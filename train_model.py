import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("dataset/urls.csv")

# Keep only benign and phishing rows
data = data[
    (data['type'] == 'benign') |
    (data['type'] == 'phishing')
]

# Keep only required columns
data = data[['url', 'type']]

# Convert labels
data['type'] = data['type'].map({
    'benign': 0,
    'phishing': 1
})

# Inputs and outputs
X = data['url']
y = data['type']

# Convert URLs into vectors
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Save model and vectorizer
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\n✅ Model and vectorizer saved successfully!")