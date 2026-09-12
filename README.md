🛡️ IVE — Intelligent URL Verification Engine

IVE (Intelligent URL Verification Engine) is a machine learning-based web application that analyzes URLs and predicts whether they may be legitimate or potentially phishing.

🚀 Features

- 🔍 URL analysis
- 🤖 Machine learning-based prediction
- 🛡️ Phishing URL detection
- 📊 Risk score
- 🌐 HTML, CSS and JavaScript frontend
- 🐍 Python Flask backend
- 🔗 Frontend-to-ML API integration

🧠 How It Works

User enters a URL

↓

Frontend sends the URL to the Flask API

↓

URL features are extracted

↓

Random Forest ML model analyzes the features

↓

IVE returns a prediction and risk score

↓

Result is displayed on the website

🛠️ Technologies

- HTML5
- CSS3
- JavaScript
- Python
- Flask
- Flask-CORS
- Pandas
- Scikit-learn
- Random Forest
- Joblib

📁 Project Structure

```text
IVE/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── feature_extraction.py
│   ├── train_model.py
│   ├── dataset.csv
│   └── phishing_model.pkl
│
├── .gitignore
├── requirements.txt
└── README.md
