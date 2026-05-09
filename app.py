from flask import Flask, render_template, request
import joblib

# Load trained model
model = joblib.load("model/phishing_model.pkl")

# Load vectorizer
vectorizer = joblib.load("model/vectorizer.pkl")

# Create Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    # Convert URL into vector
    url_vector = vectorizer.transform([url])

    # Predict
    prediction = model.predict(url_vector)[0]

    # Result
    if prediction == 1:
        result = "⚠️ PHISHING WEBSITE DETECTED"
    else:
        result = "✅ SAFE WEBSITE"

    return render_template("index.html", prediction_text=result)

# Run app
if __name__ == "__main__":
    app.run(debug=True)