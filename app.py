
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="chennai_house_price_model.pkl",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 chennai_house_price_model.pkl")
st.write(
    "Estimate a property's price using its city, size, "
    "property type, and other details."
)

MODEL_PATH = Path(__file__).parent / "chennai_house_price_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception:
    st.error(
        "The model could not be loaded. Check that "
        "indian_house_price_model_small.pkl is in the repository."
    )
    st.stop()

with st.form("house_form"):
    city = st.selectbox(
        "City",
        [
            "Ahmedabad", "Bangalore", "Chandigarh", "Chennai",
            "Delhi", "Hyderabad", "Jaipur", "Kolkata",
            "Mumbai", "Pune"
        ]
    )

    locality_type = st.selectbox(
        "Locality type",
        ["Affordable", "Mid-Range", "Premium"]
    )

    property_type = st.selectbox(
        "Property type",
        [
            "Apartment", "Builder Floor",
            "Independent House", "Villa"
        ]
    )

    bhk = st.number_input("Bedrooms (BHK)", 1, 10, 2)
    bathrooms = st.number_input("Bathrooms", 1, 10, 2)

    super_area = st.number_input(
        "Super area (sq. ft.)", min_value=100.0,
        max_value=50000.0, value=1000.0, step=50.0
    )

    carpet_area = st.number_input(
        "Carpet area (sq. ft.)", min_value=50.0,
        max_value=40000.0, value=800.0, step=50.0
    )

    floor_number = st.number_input(
        "Floor number", min_value=0, max_value=100, value=2
    )

    total_floors = st.number_input(
        "Total floors", min_value=1, max_value=100, value=5
    )

    age = st.number_input(
        "Property age (years)", min_value=0, max_value=150, value=5
    )

    furnishing = st.selectbox(
        "Furnishing status",
        ["Unfurnished", "Semi-Furnished", "Furnished"]
    )

    parking = st.selectbox("Parking available?", [0, 1])
    lift = st.selectbox("Lift available?", [0, 1])
    gated = st.selectbox("Gated community?", [0, 1])

    metro_distance = st.number_input(
        "Distance to metro (km)", 0.0, 100.0, 2.0, step=0.5
    )

    center_distance = st.number_input(
        "Distance to city center (km)", 0.0, 200.0, 5.0, step=0.5
    )

    submitted = st.form_submit_button("Predict House Price")

if submitted:
    if floor_number > total_floors:
        st.error("Floor number cannot exceed total floors.")
    elif carpet_area > super_area:
        st.error("Carpet area should not exceed super area.")
    else:
        input_data = pd.DataFrame([{
            "City": city,
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
            price = float(model.predict(input_data)[0])
            if price <= 0:
                st.error("The model returned an invalid price.")
            else:
                st.success(f"Estimated price: ₹{price:.2f} lakhs")
                st.caption(
                    "This is a machine-learning estimate based on the "
                    "training dataset, not a verified market valuation."
                )
        except Exception as e:
            st.error(f"Prediction failed: {e}")
