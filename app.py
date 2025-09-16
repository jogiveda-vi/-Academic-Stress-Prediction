from flask import Flask, request, render_template
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('stress_model.pkl', 'rb'))  # Make sure stress_model.pkl exists

# Initialize LabelEncoders with classes used during training
le_env = LabelEncoder()
le_env.classes_ = np.array(['Noisy', 'Peaceful'])

le_habits = LabelEncoder()
le_habits.classes_ = np.array(['No', 'Yes'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    peer_pressure = int(request.form['peer_pressure'])
    home_pressure = int(request.form['home_pressure'])
    study_env = le_env.transform([request.form['study_env']])[0]
    bad_habits = le_habits.transform([request.form['bad_habits']])[0]

    input_features = np.array([[peer_pressure, home_pressure, study_env, bad_habits]])
    prediction = model.predict(input_features)[0]

    return f"<h2>Predicted Academic Stress Level: {prediction}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
