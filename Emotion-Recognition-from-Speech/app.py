import os
import librosa
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Assuming the dataset is organized in a directory structure
# where each subdirectory corresponds to an emotion category
dataset_path = 'ravdess-data'

# Load the dataset
def load_data(dataset_path):
    labels = []
    features = []
    for emotion_dir in os.listdir(dataset_path):
        emotion_path = os.path.join(dataset_path, emotion_dir)
        if os.path.isdir(emotion_path):
            for file_name in os.listdir(emotion_path):
                file_path = os.path.join(emotion_path, file_name)
                if file_path.endswith('.wav'):
                    # Load the audio file
                    signal, sample_rate = librosa.load(file_path, sr=22050)
                    # Extract MFCC features
                    mfccs = librosa.feature.mfcc(signal, sr=sample_rate, n_mfcc=13)
                    features.append(np.mean(mfccs.T, axis=0))
                    labels.append(emotion_dir)
    return np.array(features), np.array(labels)

features, labels = load_data(dataset_path)

# Encode the labels
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)
labels_categorical = to_categorical(labels_encoded)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels_categorical, test_size=0.2, random_state=42)

# Define the CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(13, 1, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(len(np.unique(labels)), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Reshape the data to fit the model
X_train_reshaped = X_train.reshape(X_train.shape[0], 13, 1, 1)
X_test_reshaped = X_test.reshape(X_test.shape[0], 13, 1, 1)

# Train the model
history = model.fit(X_train_reshaped, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test_reshaped, y_test)
print(f'Test Accuracy: {test_accuracy}')
