# House Price Prediction Web Application

A Machine Learning–powered web application that predicts house prices based on user inputs such as area, number of bedrooms, and bathrooms.  
The trained model is deployed using **Flask**, allowing users to interact with it through a simple web interface.

---

## Project Overview

House price prediction is a common real-world Machine Learning problem.  
This project demonstrates the **complete ML lifecycle**:

- Data preprocessing
- Model training
- Model serialization
- Web deployment using Flask

Users can enter house details in a web form and instantly get a predicted house price.

---

##  Features

- Trained Machine Learning regression model
- Flask-based backend
- Simple and clean HTML frontend
- Real-time predictions
- Easy to deploy and extend

---

##  Tech Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Model Serialization:** Pickle

---

##  Project Structure
```
house_price_app/
│
├── app.py # Flask application
├── model_.sav # Trained ML model
├── requirements.txt # Project dependencies
│
├── templates/
│ └── index.html # Frontend UI
│
└── static/ # Static files (CSS, images if needed)
```


---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/mohankalimuthu/house-price-prediction-app.git
cd house-price-prediction-app
```
## Create Virtual Environment
```
python -m venv venv
source venv/bin/activate      # For Linux / Mac
venv\Scripts\activate         # For Windows
```

## Install Dependencies
```
pip install -r requirements.txt
```
## Run the Application
```
python app.py
```

### How It Works

1. User enters house details (area, bedrooms, bathrooms)
2. Flask receives the input from the form
3. Input data is converted into NumPy array
4. Saved ML model (model_.sav) makes the prediction
5. Predicted house price is displayed on the web page

## Model Details

**Type:** Regression Model

Trained using Scikit-learn

Saved using Pickle for deployment

Loaded directly into Flask backend

## Future Enhancements
* Add data scaling pipeline
* Improve UI using Bootstrap
* Add REST API using FastAPI
* Deploy on cloud platforms (Render, AWS, Hugging Face)
* Add database for storing predictions


## Author
**Mohan K**  
-  Email: mohankalimuthu2004@gmail.com  
-  LinkedIn: https://www.linkedin.com/in/mohan-kalimuthu/
-  GitHub: https://github.com/mohankalimuthu

## Contributing

Contributions are welcome!

If you want to improve the model or add visual dashboards, open a pull request.

## License

This project is open-source under the MIT License.

## Support

If you like this project, please star ⭐ the repository —> **it motivates further development!**
