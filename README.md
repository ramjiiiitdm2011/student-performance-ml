Student Performance Prediction – Machine Learning Web Application
Overview

This project predicts student performance using machine learning techniques. By analyzing demographic and academic features, the model estimates a student's final performance score. The project includes a complete ML pipeline and a Flask web application for real-time predictions.

Objectives

Analyze factors affecting student performance

Predict final exam scores

Build a scalable ML pipeline

Provide a user-friendly web interface for predictions

Dataset Description

Each record includes:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Math Score

Reading Score

Writing Score

Target Variable: Final Performance Score

Project Structure

artifacts — saved model and preprocessor

logs — log files

notebook — EDA and experimentation

src — ML pipeline code

components

utils.py

exception.py

logger.py

templates — web UI

index.html

app.py — Flask web application

predict.py — prediction script

requirements.txt

README.md

Workflow

Raw Data

Exploratory Data Analysis

Data Cleaning and Preprocessing

Train-Test Split

ML Pipeline (Scaling and Encoding)

Model Training and Evaluation

Save Artifacts (model.pkl, preprocessor.pkl)

Flask Web App for Prediction

Web Application

The web interface allows users to:

Enter student details and scores

Submit the form

View predicted performance in the browser

Model Performance

Evaluation metrics used:

R² Score

RMSE

MAE

(You can update these values later.)

Tech Stack

Python

Pandas, NumPy

Scikit-Learn

Flask

HTML (Jinja Templates)

Git and GitHub

VS Code / Codespaces

How to Run the Project
1. Clone the Repository
git clone <repo-url>
cd student-performance-ml

2. Install Dependencies
pip install -r requirements.txt

3. Run the Web Application
python app.py

4. Open in Browser

Local: http://127.0.0.1:5000

Codespaces: Use the forwarded port link

Optional: Run Prediction Script
python predict.py

Future Enhancements

UI styling with Bootstrap

Deployment on Render or Railway

Feature importance visualization

Hyperparameter tuning

Author

Ramji Lal Jhanginia