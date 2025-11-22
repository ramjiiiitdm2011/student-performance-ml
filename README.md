📘 Student Performance Prediction – End-to-End Machine Learning Web Application
🧠 Overview

This project predicts student performance using Machine Learning techniques. By analyzing demographic, behavioral, and academic factors, the model estimates a student’s final score and uncovers insights that influence learning outcomes.

✅ Complete ML pipeline
✅ Automated preprocessing & model training
✅ Saved model artifacts
✅ Flask-based web application for real-time prediction

🎯 Objectives

Analyze factors affecting student performance

Build a regression model to predict final scores

Create a modular, scalable ML pipeline

Develop a user-friendly web interface for predictions

📊 Dataset Description

Each row represents a student with features affecting academic performance.

Key Features

Gender

Race/Ethnicity

Parental Education

Lunch Type

Test Preparation Course

Math Score

Reading Score

Writing Score

Target Variable

✅ Final performance score

🧱 Updated Project Architecture
student-performance-ml/
│
├── artifacts/                # Saved model & preprocessor
├── logs/                     # Log files
├── notebook/                 # EDA & experimentation
├── src/                      # Modular ML pipeline components
│   ├── components/
│   ├── utils.py
│   ├── exception.py
│   └── logger.py
├── templates/                # ✅ Web UI templates
│   └── index.html
├── app.py                    # ✅ Flask web application
├── predict.py                # Prediction script
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
Flask Web App for Prediction ✅

🌐 Web Application

A browser-based interface allows users to:

✅ Select demographic and preparation factors
✅ Enter exam scores
✅ Click Predict
✅ View predicted performance instantly

UI Screenshot (Optional)

You can insert the form screenshot here later.

📈 Model Performance

Metrics used:

R² Score

RMSE

MAE

✅ (Replace with actual values when finalized)

🛠️ Tech Stack

Python

Pandas / NumPy

Scikit-Learn

Flask ✅

HTML / Jinja Templates ✅

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

Flask will start on port 5000.
If using Codespaces:
✅ Click Open in Browser from forwarded port link.

You should see the web form UI.

🧪 Optional: Run Prediction Script
python predict.py

🔮 Future Enhancements

UI styling with Bootstrap

Deployment on Render/Railway

Feature importance visualization

Hyperparameter tuning

Model versioning & monitoring

🧑‍💻 Author

Ramji Lal Jhanginia