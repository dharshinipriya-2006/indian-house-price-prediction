
import os
import joblib
import pandas as pd
import streamlit as st


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CasaMetric | Chennai Property Intelligence",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# 2. MODEL CONFIGURATION
# =========================================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "chennai_house_price_model.pkl"
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except FileNotFoundError:
    st.error(
        "Model file not found. Please ensure "
        "'chennai_house_price_model.pkl' is in the same folder as app.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Unable to load the prediction model: {error}")
    st.stop()

# =========================================================
# 3. PREMIUM LUXURY DESIGN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --navy: #0b1424;
    --navy-light: #14243a;
    --emerald: #0d9877;
    --emerald-light: #18b58f;
    --gold: #d6b36a;
    --cream: #f7f5ef;
    --muted: #9aa9bc;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--cream);
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide default Streamlit elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Hero section */

.hero {
    background: linear-gradient(120deg, #0b1424, #142c40);
    padding: 55px;
    border-radius: 22px;
    color: white;
    margin-bottom: 30px;
    border: 1px solid rgba(214,179,106,0.25);
}

.hero-label {
    color: #d6b36a;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 18px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 600;
    color: white;
    margin-bottom: 12px;
}

.hero p {
    color: #c3cfdb;
    font-size: 16px;
    line-height: 1.8;
    max-width: 650px;
}

.hero-highlight {
    color: #18b58f;
}

/* Section headings */

.section-heading {
    color: #0b1424;
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 6px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 22px;
}

/* Information cards */

.info-card {
    background: white;
    border: 1px solid #e8e4d9;
    border-radius: 15px;
    padding: 22px;
    min-height: 115px;
    box-shadow: 0 4px 15px rgba(11,20,36,0.04);
}

.info-label {
    color: #64748b;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.info-value {
    color: #0b1424;
    font-size: 22px;
    font-weight: 800;
    margin-top: 9px;
}

/* Form */

div[data-testid="stForm"] {
    background: white;
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #e8e4d9;
    box-shadow: 0 5px 20px rgba(11,20,36,0.04);
}

.stSelectbox label,
.stNumberInput label {
    color: #26364b !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    border-radius: 9px !important;
}

/* Predict button */

.stFormSubmitButton button {
    background: linear-gradient(100deg, #0d9877, #08775e);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 13px 25px;
    font-size: 16px;
    font-weight: 700;
    width: 100%;
}

.stFormSubmitButton button:hover {
    background: #075f4c;
    color: white;
}

/* Prediction result */

.result-card {
    background: linear-gradient(120deg, #0b1424, #173b43);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-top: 28px;
    border: 1px solid rgba(214,179,106,0.35);
}

.result-label {
    color: #d6b36a;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.result-price {
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 43px;
    font-weight: 700;
    margin-top: 10px;
}

.result-description {
    color: #c3cfdb;
    font-size: 14px;
    margin-top: 10px;
}

/* Result metrics */

.metric-card {
    background: white;
    border: 1px solid #e8e4d9;
    padding: 20px;
    border-radius: 13px;
    margin-top: 15px;
}

.metric-label {
    color: #64748b;
    font-size: 12px;
    font-weight: 600;
}

.metric-value {
    color: #0b1424;
    font-size: 21px;
    font-weight: 800;
    margin-top: 7px;
}

/* Footer */

.footer {
    text-align: center;
    color: #718096;
    font-size: 12px;
    padding-top: 35px;
    margin-top: 45px;
    border-top: 1px solid #e5e0d5;
}

.footer strong {
    color: #0d9877;
}

</style>
""", unsafe_allow_html=True)



# =========================================================
# 4. HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-label">CHENNAI REAL ESTATE INTELLIGENCE</div>

    <h1>
        Discover the True Value of Your
        <span class="hero-highlight">Property.</span>
    </h1>

    <p>
        Smarter property decisions start with better insights.
        CasaMetric uses machine learning to estimate Chennai
        property values based on location, property features,
        and accessibility.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 4. HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-label">CHENNAI REAL ESTATE INTELLIGENCE</div>

    <h1>Find the True Value of Your <span class="hero-highlight">Property.</span></h1>

    <p>
        Make smarter property decisions with CasaMetric.
        Our machine learning-powered platform estimates
        Chennai property prices using important property
        characteristics and location factors.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 5. INFORMATION CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">LOCATION</div>
        <div class="info-value">Chennai, India</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">TECHNOLOGY</div>
        <div class="info-value">Machine Learning</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">PLATFORM</div>
        <div class="info-value">CasaMetric AI</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 6. PROPERTY INPUT SECTION
# =========================================================

st.markdown("""
<div class="section-heading">Property Details</div>
<div class="section-subtitle">
Enter your property information to receive an estimated market value.
</div>
""", unsafe_allow_html=True)


with st.form("property_form"):

    st.markdown("#### 01 — Location & Property Type")

    col1, col2 = st.columns(2)

    with col1:
        city = "Chennai"

        locality_type = st.selectbox(
            "Locality Category",
            ["Affordable", "Mid-Range", "Premium"]
        )

        property_type = st.selectbox(
            "Property Type",
            ["Apartment", "Independent House", "Villa", "Builder Floor"]
        )

    with col2:
        furnishing_status = st.selectbox(
            "Furnishing Status",
            ["Furnished", "Semi-Furnished", "Unfurnished"]
        )

        bhk = st.number_input(
            "Number of Bedrooms (BHK)",
            min_value=1,
            max_value=20,
            value=2,
            step=1
        )

    st.markdown("---")
    st.markdown("#### 02 — Area & Structure")

    col1, col2 = st.columns(2)

    with col1:
        bathrooms = st.number_input(
            "Number of Bathrooms",
            min_value=1,
            max_value=20,
            value=2,
            step=1
        )

        super_area = st.number_input(
            "Super Built-up Area (Sq.Ft.)",
            min_value=100,
            max_value=50000,
            value=1200,
            step=50
        )

    with col2:
        carpet_area = st.number_input(
            "Carpet Area (Sq.Ft.)",
            min_value=100,
            max_value=50000,
            value=1000,
            step=50
        )

        age_of_property = st.number_input(
            "Property Age (Years)",
            min_value=0,
            max_value=100,
            value=5,
            step=1
        )

    col1, col2 = st.columns(2)

    with col1:
        floor_number = st.number_input(
            "Current Floor Number",
            min_value=0,
            max_value=100,
            value=2,
            step=1
        )

    with col2:
        total_floors = st.number_input(
            "Total Number of Floors",
            min_value=1,
            max_value=100,
            value=5,
            step=1
        )

    st.markdown("---")
    st.markdown("#### 03 — Amenities & Accessibility")

    col1, col2, col3 = st.columns(3)

    with col1:
        parking = st.selectbox(
            "Parking Available",
            ["Yes", "No"]
        )

    with col2:
        lift_available = st.selectbox(
            "Lift Available",
            ["Yes", "No"]
        )

    with col3:
        gated_community = st.selectbox(
            "Gated Community",
            ["Yes", "No"]
        )

    col1, col2 = st.columns(2)

    with col1:
        distance_to_metro = st.number_input(
            "Distance to Metro (Km)",
            min_value=0.0,
            max_value=100.0,
            value=2.0,
            step=0.5
        )

    with col2:
        distance_to_city_center = st.number_input(
            "Distance to City Center (Km)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.5
        )

    st.markdown("---")

    submitted = st.form_submit_button(
        "Estimate Property Value"
    )


# =========================================================
# 7. PREDICTION LOGIC
# =========================================================

if submitted:

    if carpet_area > super_area:
        st.error(
            "Carpet area cannot be greater than the super built-up area. "
            "Please correct the area values."
        )

    elif floor_number > total_floors:
        st.error(
            "Current floor number cannot exceed the total number of floors."
        )

    else:

        # Convert Yes/No values into the model's numeric format

        parking_value = 1 if parking == "Yes" else 0

        lift_value = 1 if lift_available == "Yes" else 0

        gated_value = 1 if gated_community == "Yes" else 0


        # Create input DataFrame using the exact original model features

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
            "Age_of_Property": age_of_property,
            "Furnishing_Status": furnishing_status,
            "Parking": parking_value,
            "Lift_Available": lift_value,
            "Gated_Community": gated_value,
            "Distance_to_Metro_km": distance_to_metro,
            "Distance_to_City_Center_km": distance_to_city_center
        }])


        try:

            # Predict property price

            prediction = float(model.predict(input_data)[0])

            # Display prediction

            if prediction <= 0:
                st.error(
                    "The model returned an invalid price. "
                    "Please check the property details."
                )

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

                    <div class="result-description">
                        Estimated market value based on your property details
                        and the trained machine learning model.
                    </div>
                </div>
                """, unsafe_allow_html=True)


                # Additional result metrics

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            PRICE PER SQ.FT.
                        </div>
                        <div class="metric-value">
                            ₹ {price_per_sqft:,.0f}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            PROPERTY AREA
                        </div>
                        <div class="metric-value">
                            {super_area:,.0f} Sq.Ft.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            PROPERTY TYPE
                        </div>
                        <div class="metric-value">
                            {property_type}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


                st.success(
                    "Property price estimation completed successfully."
                )

                st.info(
                    "Note: This is an ML-based estimated value, "
                    "not an official property valuation or guaranteed selling price."
                )

        except Exception as error:
            st.error(
                f"Prediction failed. Please check the input data and model compatibility. "
                f"Error: {error}"
            )


# =========================================================
# 8. FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <strong>CasaMetric</strong> — Chennai Property Intelligence

    <br><br>

    Powered by Machine Learning | Built with Python & Streamlit

    <br><br>

    © 2026 CasaMetric. For educational and estimation purposes only.
</div>
""", unsafe_allow_html=True)

