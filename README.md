📘 Student Performance Prediction – End-to-End Machine Learning Web Application
🧠 Overview

This project predicts student performance using Machine Learning techniques. By analyzing demographic, behavioral, and academic factors, the model estimates a student’s final score and provides insights that can support educational decisions.

The project includes:

End-to-end ML pipeline

Automated preprocessing and model training

Saved model artifacts

Flask-based web application for real-time prediction

🎯 Objectives

Analyze factors affecting student performance

Predict final exam scores

Build a modular, scalable ML pipeline

Provide a web-based interface for user input and prediction

📊 Dataset Description

Each record in the dataset represents a student and includes:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Math Score

Reading Score

Writing Score

Target Variable

Final Performance Score

🧱 Project Architecture
student-performance-ml/
│
├── artifacts/                # Saved model & preprocessor
├── logs/                     # Log files
├── notebook/                 # EDA & experimentation
├── src/
│   ├── components/
│   ├── utils.py
│   ├── exception.py
│   └── logger.py
├── templates/
│   └── index.html            # Web UI template
├── app.py                    # Flask web application
├── predict.py                # Script for manual predictions
├── requirements.txt
└── README.md

🚀 Workflow
Raw Data
    ↓
Exploratory Data Analysis (EDA)
    ↓
Data Cleaning & Preprocessing
    ↓
Train-Test Split
    ↓
ML Pipeline (Scaling + Encoding)
    ↓
Model Training & Evaluation
    ↓
Save Artifacts (model.pkl, preprocessor.pkl)
    ↓
Flask Web App for Prediction

🌐 Web Application

A browser-based interface allows users to:

Select demographic and preparation factors

Enter exam scores

Click “Predict”

View predicted performance instantly

UI Screenshot

(You can insert the screenshot here later.)

📈 Model Performance

Evaluation metrics used:

R² Score

RMSE

MAE

(You may update with actual values.)

🛠️ Tech Stack

Python

Pandas / NumPy

Scikit-Learn

Flask

HTML / Jinja Templates

Git & GitHub

VS Code / Codespaces

📥 How to Run the Project
1️⃣ Clone the Repository
git clone <repo-url>
cd student-performance-ml

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Web Application
python app.py

4️⃣ Open in Browser

If running locally: open http://127.0.0.1:5000

If using Codespaces: click Open in Browser from the forwarded port

You will see the prediction form.

🧪 Optional: Run Prediction Script
python predict.py

🔮 Future Enhancements

UI styling (Bootstrap)

Deployment on Render / Railway

Model explainability (Feature Importance)

Hyperparameter tuning

Model monitoring & versioning

👤 Author

Ramji Lal Jhanginia