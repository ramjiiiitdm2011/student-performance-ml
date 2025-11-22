from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load artifacts
model = pickle.load(open('artifacts/model.pkl', 'rb'))
preprocessor = pickle.load(open('artifacts/preprocessor.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return "✅ Student Performance Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    transformed = preprocessor.transform(df)
    result = model.predict(transformed)
    return jsonify({"prediction": float(result[0])})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

