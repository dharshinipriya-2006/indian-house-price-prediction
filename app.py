import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Chennai Estate | Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f4f7fb;
}

.block-container {
    max-width: 1150px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    background: linear-gradient(120deg, #101e3d, #183d63);
    padding: 38px 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero-tag {
    color: #69dfd0;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    color: white;
    font-size: 34px;
    font-weight: 800;
    margin: 12px 0;
}

.hero p {
    color: #d2deed;
    font-size: 15px;
    margin-bottom: 0;
}

.section-title {
    color: #142b49;
    font-size: 21px;
    font-weight: 800;
    margin-top: 15px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #75849a;
    font-size: 13px;
    margin-bottom: 20px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #e5ebf3;
    border-radius: 15px;
    padding: 17px;
}

.stSelectbox label, .stNumberInput label {
    color: #263b59 !important;
    font-weight: 600 !important;
}

div[data-testid="stButton"] button {
    background: linear-gradient(90deg, #087e83, #13a89b);
    color: white;
    border: none;
    border-radius: 10px;
    height: 52px;
    font-size: 16px;
    font-weight: 700;
    width: 100%;
}

div[data-testid="stButton"] button:hover {
    background: #076a70;
    color: white;
    border: none;
}

.result-card {
    background: linear-gradient(120deg, #102344, #174b66);
    padding: 30px;
    border-radius: 18px;
    color: white;
    margin-top: 25px;
    text-align: center;
}

.result-label {
    color: #a8d9df;
    font-size: 14px;
    font-weight: 600;
}

.result-price {
    font-size: 39px;
    font-weight: 800;
    color: #ffffff;
    margin: 12px 0;
}

.result-note {
    color: #c9d9e8;
    font-size: 12px;
}

.footer {
    text-align: center;
    color: #8996a8;
    font-size: 12px;
    margin-top: 45px;
}

hr {
    border-color: #e3eaf2;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD ML MODEL ----------------

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
    st.error(f"Unable to load prediction model: {e}")
    st.stop()


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">CHENNAI REAL ESTATE INTELLIGENCE</div>
    <h1>Find Your Property's True Potential.</h1>
    <p>
        Smart property valuation powered by Machine Learning.
        Enter your property details and discover its estimated market value.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- TOP INFORMATION ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Location", "Chennai")

with col2:
    st.metric("Technology", "Machine Learning")

with col3:
    st.metric("Model", "Price Prediction")

st.divider()


# ---------------- PROPERTY FORM ----------------

st.markdown(
    '<div class="section-title">🏠 Property Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Provide accurate details to get a better estimate.</div>',
    unsafe_allow_html=True
)

with st.form("property_form"):

    # BASIC DETAILS

    st.markdown("### 📍 Basic Details")

    c1, c2 = st.columns(2)

    with c1:
        locality_type = st.selectbox(
            "Locality Type",
            ["Affordable", "Mid-Range", "Premium"]
        )

        property_type = st.selectbox(
            "Property Type",
            [
                "Apartment",
                "Independent House",
                "Villa",
                "Builder Floor"
            ]
        )

    with c2:
        bhk = st.number_input(
            "Bedrooms (BHK)",
            min_value=1,
            max_value=10,
            value=2
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=10,
            value=2
        )

    st.divider()

    # AREA DETAILS

    st.markdown("### 📐 Area Details")

    c1, c2 = st.columns(2)

    with c1:
        super_area = st.number_input(
            "Super Area (sq. ft.)",
            min_value=100.0,
            max_value=50000.0,
            value=1000.0,
            step=50.0
        )

    with c2:
        carpet_area = st.number_input(
            "Carpet Area (sq. ft.)",
            min_value=50.0,
            max_value=50000.0,
            value=800.0,
            step=50.0
        )

    st.divider()

    # BUILDING DETAILS

    st.markdown("### 🏢 Building Details")

    c1, c2, c3 = st.columns(3)

    with c1:
        floor_number = st.number_input(
            "Floor Number",
            min_value=0,
            max_value=100,
            value=1
        )

    with c2:
        total_floors = st.number_input(
            "Total Floors",
            min_value=1,
            max_value=100,
            value=5
        )

    with c3:
        age = st.number_input(
            "Property Age (years)",
            min_value=0,
            max_value=150,
            value=5
        )

    furnishing = st.selectbox(
        "Furnishing Status",
        ["Furnished", "Semi-Furnished", "Unfurnished"]
    )

    st.divider()

    # AMENITIES

    st.markdown("### ✨ Amenities")

    c1, c2, c3 = st.columns(3)

    with c1:
        parking = st.selectbox(
            "🚗 Parking",
            [0, 1],
            format_func=lambda x: "Available" if x == 1 else "Not Available"
        )

    with c2:
        lift = st.selectbox(
            "🛗 Lift",
            [0, 1],
            format_func=lambda x: "Available" if x == 1 else "Not Available"
        )

    with c3:
        gated = st.selectbox(
            "🔐 Gated Community",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

    st.divider()

    # LOCATION DETAILS

    st.markdown("### 🚇 Location & Connectivity")

    c1, c2 = st.columns(2)

    with c1:
        metro_distance = st.number_input(
            "Distance to Metro (km)",
            min_value=0.0,
            max_value=100.0,
            value=2.0,
            step=0.5
        )

    with c2:
        center_distance = st.number_input(
            "Distance to City Center (km)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.5
        )

    st.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.form_submit_button(
        "✨ Predict Property Price"
    )


# ---------------- PREDICTION ----------------

if predict_button:

    if carpet_area > super_area:
        st.error("Carpet area cannot be greater than super area.")

    elif floor_number > total_floors:
        st.error("Floor number cannot exceed total floors.")

    else:

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

            prediction = float(model.predict(input_data)[0])

            if not pd.notna(prediction) or prediction < 0:
                st.error("The model returned an invalid price.")
            else:

                price_per_sqft = (
                    prediction * 100000 / super_area
                )

                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">
                        YOUR ESTIMATED PROPERTY VALUE
                    </div>
                    <div class="result-price">
                        ₹ {prediction:,.2f} Lakhs
                    </div>
                    <div class="result-note">
                        Machine Learning Based Property Valuation
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("### 📊 Property Valuation Summary")

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.metric(
                        "Estimated Price",
                        f"₹{prediction:.2f} L"
                    )

                with c2:
                    st.metric(
                        "Price per Sq. Ft.",
                        f"₹{price_per_sqft:,.0f}"
                    )

                with c3:
                    st.metric(
                        "Property Area",
                        f"{super_area:,.0f} sq. ft."
                    )

                st.markdown("### 🏡 Property Overview")

                st.write(f"**Property Type:** {property_type}")
                st.write(f"**Locality Category:** {locality_type}")
                st.write(f"**Bedrooms:** {bhk} BHK")
                st.write(f"**Bathrooms:** {bathrooms}")
                st.write(f"**Furnishing:** {furnishing}")
                st.write(f"**Property Age:** {age} years")

                st.success("Property price prediction completed!")

                st.caption(
                    "Disclaimer: This is a machine-learning-based estimate, "
                    "not an official market valuation or guaranteed selling price."
                )

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <hr>
    <p>CHENNAI ESTATE | AI POWERED PROPERTY VALUATION</p>
    <p>Developed using Python, Streamlit and Machine Learning</p>
</div>
""", unsafe_allow_html=True)
