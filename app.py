
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Chennai House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Chennai House Price Prediction")
st.write("Estimate a property's price in Chennai.")

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "chennai_house_price_model.pkl"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()

st.subheader("Enter Property Details")

locality_type = st.selectbox(
    "Locality Type",
    ["Affordable", "Mid-Range", "Premium"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa", "Builder Floor"]
)

bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)
bathrooms = st.number_input(
    "Bathrooms", min_value=1, max_value=10, value=2
)

super_area = st.number_input(
    "Super Area (sq ft)", min_value=100.0, value=1000.0
)
carpet_area = st.number_input(
    "Carpet Area (sq ft)", min_value=50.0, value=800.0
)

floor_number = st.number_input(
    "Floor Number", min_value=0, max_value=100, value=1
)
total_floors = st.number_input(
    "Total Floors", min_value=1, max_value=100, value=5
)
age = st.number_input(
    "Age of Property (years)", min_value=0, max_value=150, value=5
)

furnishing = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

parking = st.selectbox("Parking Available", [0, 1])
lift = st.selectbox("Lift Available", [0, 1])
gated = st.selectbox("Gated Community", [0, 1])

metro_distance = st.number_input(
    "Distance to Metro (km)", min_value=0.0, value=2.0
)
center_distance = st.number_input(
    "Distance to City Center (km)", min_value=0.0, value=5.0
)

if st.button("Predict House Price"):
    input_data = pd.DataFrame([{
        "City": "Chennai",
        "Locality_Type": locality_type,
        "Property_Type": property_type,
        "BHK": bhk,
        "Bathrooms": bathrooms,
        "Super_Area_SqFt": super_area,
        "Carpet_Area_SqFt": carpet_area,
        "Floor_Number": floor_number,
        "Total_Floors": total_floors,
        "Age_of_Property": age,
        "Furnishing_Status": furnishing,
        "Parking": parking,
        "Lift_Available": lift,
        "Gated_Community": gated,
        "Distance_to_Metro_km": metro_distance,
        "Distance_to_City_Center_km": center_distance
    }])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated House Price: ₹{prediction:.2f} lakhs")
        st.caption(
            "This is a model-based estimate, not an official market valuation."
        )
    except Exception as e:
        st.error(f"Prediction failed: {e}")
