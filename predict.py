import pickle
import pandas as pd

def load_artifacts():
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    preprocessor = pickle.load(open('artifacts/preprocessor.pkl', 'rb'))
    return model, preprocessor

def predict(input_data):
    model, preprocessor = load_artifacts()
    df = pd.DataFrame([input_data])
    transformed = preprocessor.transform(df)
    prediction = model.predict(transformed)
    return prediction[0]

if __name__ == "__main__":
    sample = {
    "gender": "female",
    "race_ethnicity": "group B",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "math_score": 72,
    "reading_score": 75,
    "writing_score": 70
}


    print("Predicted Score:", predict(sample))
