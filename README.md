# Chennai House Price Prediction

## Project Overview
A machine learning web application that estimates residential property prices in Chennai based on property features and location-related information.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Random Forest Regression
- Streamlit
- Joblib
- GitHub

## Dataset
The model was trained using 8,150 Chennai property records selected from an existing Indian housing dataset.

## Model Performance
Evaluated on a held-out test set:
- **MAE:** 29.17 lakhs
- **RMSE:** 44.80 lakhs
- **R² Score:** 0.776

These metrics reflect performance on the available dataset. They do not establish accuracy against actual Chennai property transactions.

## Features
- Property type and locality category
- Number of bedrooms and bathrooms
- Super area and carpet area
- Floor number and building age
- Furnishing, parking, lift, and gated-community information
- Distance to metro and city center
- Estimated price displayed in Indian rupees (lakhs)

## Run Locally
1. Clone this repository.
2. Install the dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `streamlit run app.py`


