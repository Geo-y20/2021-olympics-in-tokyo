from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)  # Use __name__ to initialize Flask

# Load the saved Random Forest model
with open('best_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form (you can adapt this to fit your form structure)
    discipline = int(request.form['Discipline'])
    event = int(request.form['Event'])
    
    # Prepare the features for prediction
    features = np.array([[discipline, event]])
    
    # Make the prediction
    prediction = model.predict(features)
    
    # Map the prediction to the medal type
    medal_map = {0: 'Bronze', 1: 'Gold', 2: 'Silver'}
    predicted_medal = medal_map.get(prediction[0], "Unknown")
    
    return render_template('index.html', prediction_text=f'The predicted medal type is: {predicted_medal}')

if __name__ == "__main__":  # Correct the main entry point check
    app.run(debug=True)
