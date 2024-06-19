import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)

# Data cleaning and feature selection
df.dropna(subset=['Age', 'Sex', 'Pclass', 'Survived'], inplace=True)
X = df[['Pclass', 'Sex', 'Age']]
X = pd.get_dummies(X, drop_first=True)  # One-hot encoding for 'Sex'
y = df['Survived']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Example prediction
new_data = pd.DataFrame({'Pclass': [3], 'Sex_male': [1], 'Age': [25]})
prediction = model.predict(new_data)
print("Predicted Survival (0 = No, 1 = Yes):", prediction)
