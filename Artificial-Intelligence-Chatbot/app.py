import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataset
training_data = [
    {'text': 'What is your name?', 'intent': 'name'},
    {'text': 'How are you?', 'intent': 'greeting'},
    {'text': 'What can you do?', 'intent': 'capabilities'},
    {'text': 'Goodbye!', 'intent': 'goodbye'}
]

# Preprocessing function
def preprocess(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

# Preprocess training data
X_train = [preprocess(data['text']) for data in training_data]
y_train = [data['intent'] for data in training_data]

# Vectorization (using TF-IDF)
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

from sklearn.naive_bayes import MultinomialNB

# Train a classifier (Naive Bayes for example)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

def chatbot_response(input_text):
    # Preprocess input
    preprocessed_input = preprocess(input_text)
    # Vectorize input
    input_vector = vectorizer.transform([preprocessed_input])
    # Predict intent
    predicted_intent = classifier.predict(input_vector)[0]
    # Generate response based on intent
    if predicted_intent == 'name':
        return "My name is Chatbot."
    elif predicted_intent == 'greeting':
        return "Hello! How can I help you?"
    elif predicted_intent == 'capabilities':
        return "I can assist you with basic information."
    elif predicted_intent == 'goodbye':
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that."

# Example interaction
user_input = input("User: ")
while user_input.lower() != 'exit':
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    user_input = input("User: ")
