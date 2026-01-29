from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model_.sav', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    input_data = np.array([[area, bedrooms, bathrooms]])

    prediction = model.predict(input_data)[0]

    return render_template(
        'index.html',
        prediction_text=f'Estimated House Price: ₹ {prediction:,.2f}'
    )

if __name__ == '__main__':
    app.run(debug=True)
