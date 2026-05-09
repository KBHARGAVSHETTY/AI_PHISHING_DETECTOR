# AI Phishing URL Detector

A machine learning-based web application that identifies whether a URL is legitimate or phishing.

The project uses TF-IDF vectorization and Logistic Regression for URL classification and is built using Flask for the web interface.

## Features

- URL phishing detection
- Machine learning-based classification
- Flask web application
- Real-time prediction
- Simple and responsive interface

## Tech Stack

- Python
- Flask
- scikit-learn
- pandas
- HTML/CSS

## Project Structure

```text
AI_PHISHING_DETECTOR/
│
├── dataset/
├── model/
├── templates/
├── static/
├── utils/
├── app.py
├── train_model.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/KBHARGAVSHETTY/AI_PHISHING_DETECTOR.git
```

Move into the project directory:

```bash
cd AI_PHISHING_DETECTOR
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask pandas scikit-learn joblib
```

## Running the Project

Train the model:

```bash
python train_model.py
```

Start the Flask application:

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Model Details

- TF-IDF Vectorizer
- Logistic Regression Classifier
- Binary classification:
  - Safe URL
  - Phishing URL

## Future Improvements

- Feature-based URL analysis
- Confidence score prediction
- Browser extension integration
- Deployment support

## Author

Bhargav Shetty

GitHub:
https://github.com/KBHARGAVSHETTY
