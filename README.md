Academic Stress Level Predictor
Project Overview:
This project aims to predict the academic stress level of students using a Naive Bayes Classifier based on important factors such as:
Peer Pressure,Academic Pressure from Home,Study Environment,Lifestyle Habits (e.g., Smoking, Drinking)
The solution is designed to help educational institutions and counselors provide timely support to students by predicting stress levels and offering actionable insights.

How It Works
1. Data Preprocessing:
Categorical inputs like study environment and bad habits are encoded into numeric values for machine learning processing. Missing data is handled by replacing with default values.
2. Model Training:
A Gaussian Naive Bayes Classifier is trained on real student data and evaluated using accuracy, precision, recall, and F1-score.
3. Web Interface:
A simple HTML form allows users to input key metrics. The backend, powered by Flask, predicts the academic stress level in real time.

Technologies Used:
Python 3
Scikit-learn
Flask
HTML 
