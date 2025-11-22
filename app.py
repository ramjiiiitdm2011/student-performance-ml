from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('artifacts/model.pkl', 'rb'))
preprocessor = pickle.load(open('artifacts/preprocessor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        "gender": request.form['gender'],
        "race_ethnicity": request.form['race_ethnicity'],
        "parental_level_of_education": request.form['parental_level_of_education'],
        "lunch": request.form['lunch'],
        "test_preparation_course": request.form['test_preparation_course'],
        "math_score": float(request.form['math_score']),
        "reading_score": float(request.form['reading_score']),
        "writing_score": float(request.form['writing_score'])
    }

    df = pd.DataFrame([data])
    transformed = preprocessor.transform(df)
    result = model.predict(transformed)

    return render_template('index.html', prediction=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
