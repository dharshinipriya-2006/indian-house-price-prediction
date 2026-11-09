
import streamlit as st
import pandas as pd
import joblib
import os

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CasaMetric | Chennai Property Valuation",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. PREMIUM LUXURY DESIGN
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

/* Hide default decoration */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* HERO SECTION */

.hero {
    background:
        radial-gradient(circle at 90% 10%, rgba(24,181,143,0.20), transparent 32%),
        linear-gradient(125deg, #091323, #132943 65%, #173b43);
    padding: 55px 45px;
    border-radius: 22px;
    color: white;
    border: 1px solid rgba(214,179,106,0.22);
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}

.hero-tag {
    display: inline-block;
    color: #d6b36a;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 800;
    margin-bottom: 15px;
}

.hero h1 {
    color: #ffffff;
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 5vw, 48px);
    line-height: 1.2;
    font-weight: 700;
    margin: 5px 0 15px 0;
}

.hero h1 span {
    color: #37c59e;
}

.hero p {
    color: #c3cfdb;
    font-size: 15px;
    line-height: 1.8;
    max-width: 650px;
}

.hero-bottom {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 25px;
}

.hero-pill {
    padding: 8px 14px;
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 30px;
    color: #e4eaf0;
    font-size: 12px;
    background: rgba(255,255,255,0.05);
}

/* INFORMATION CARDS */

.info-card {
    background: #ffffff;
    border: 1px solid #e8e5dc;
    border-radius: 15px;
    padding: 19px;
    min-height: 110px;
    box-shadow: 0 4px 16px rgba(11,20,36,0.035);
}

.info-label {
    color: #7c8795;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.info-value {
    color: #14243a;
    font-size: 20px;
    font-weight: 800;
    margin-top: 10px;
}

.info-description {
    color: #929ba7;
    font-size: 11px;
    margin-top: 4px;
}

/* SECTION HEADINGS */

.section-heading {
    color: #13243b;
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 5px;
}

.section-description {
    color: #89929f;
    font-size: 13px;
    margin-bottom: 20px;
}

.section-label {
    color: #0d9877;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* FORM CONTAINER */

div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #e7e5dd;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 8px 30px rgba(11,20,36,0.045);
}

/* INPUT LABELS */

.stSelectbox label,
.stNumberInput label {
    color: #24354b !important;
    font-weight: 700 !important;
    font-size: 13px !important;
}

/* INPUT BOXES */

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 9px;
    border-color: #dce2e8;
    background: #ffffff;
}

div[data-baseweb="select"] > div:hover,
div[data-baseweb="input"] > div:hover {
    border-color: #0d9877;
}

/* FORM SUBMIT BUTTON */

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(110deg, #087b64, #13a982);
    color: white;
    border: none;
    border-radius: 11px;
    height: 54px;
    font-size: 15px;
    font-weight: 800;
    width: 100%;
    transition: 0.2s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: linear-gradient(110deg, #066b57, #0d9472);
    color: white;
    border: none;
}

/* PREDICTION RESULT */

.result-card {
    background:
        radial-gradient(circle at 90% 10%, rgba(24,181,143,0.19), transparent 35%),
        linear-gradient(125deg, #091323, #142d43);
    padding: 38px 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 30px;
    border: 1px solid rgba(214,179,106,0.25);
    box-shadow: 0 12px 35px rgba(11,20,36,0.12);
}

.result-eyebrow {
    color: #d6b36a;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 800;
}

.result-price {
    color: #ffffff;
    font-family: 'Playfair Display', serif;
    font-size: clamp(34px, 6vw, 48px);
    font-weight: 700;
    margin: 15px 0;
}

.result-subtitle {
    color: #b9c9d8;
    font-size: 13px;
}

/* RESULT METRICS */

.result-metric {
    background: #ffffff;
    border: 1px solid #e7e5dd;
    border-radius: 14px;
    padding: 20px;
    min-height: 105px;
}

.result-metric-label {
    color: #87919e;
    font-size: 11px;
    letter-spacing: 1px;
    font-weight: 700;
    text-transform: uppercase;
}

.result-metric-value {
    color: #12243b;
    font-size: 21px;
    font-weight: 800;
    margin-top: 10px;
}

/* PROPERTY OVERVIEW */

.overview-card {
    background: white;
    padding: 23px;
    border: 1px solid #e7e5dd;
    border-radius: 15px;
    margin-top: 18px;
}

.overview-title {
    color: #14243a;
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 16px;
}

.overview-item {
    color: #596678;
    font-size: 13px;
    padding: 11px 0;
    border-bottom: 1px solid #edf0f2;
}

.overview-item b {
    color: #172b42;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 30px 10px 10px 10px;
    margin-top: 45px;
    border-top: 1px solid #e5e4dd;
}

.footer-brand {
    color: #14243a;
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: 2px;
}

.footer-text {
    color: #8b95a2;
    font-size: 11px;
    margin-top: 8px;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* MOBILE */

@media (max-width: 768px) {

    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }

    .hero {
        padding: 32px 22px;
    }

    .hero h1 {
        font-size: 32px;
    }

    div[data-testid="stForm"] {
        padding: 15px;
    }

    .result-card {
        padding: 28px 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD EXISTING MACHINE LEARNING MODEL
# =========================================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "chennai_house_price_model.pkl"
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    if not os.path.exists(MODEL_PATH):
        st.error(
            "Model file not found. Please make sure "
            "chennai_house_price_model.pkl is in the same "
            "folder as app.py."
        )
        st.stop()

    model = load_model()

except Exception as e:
    st.error(f"Unable to load prediction model: {e}")
    st.stop()


# =========================================================
# 4. BRAND HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-tag">
        CHENNAI REAL ESTATE INTELLIGENCE
    </div>

    <h1>
        Discover the Value<br>
        Behind Your <span>Property.</span>
    </h1>

    <p>
        Experience intelligent property valuation with CasaMetric.
        Our machine learning model analyzes your property details
        to estimate its potential market value in Chennai.
    </p>

    <div class="hero-bottom">
        <div class="hero-pill">✦ AI Powered Valuation</div>
        <div class="hero-pill">⌖ Chennai Property Market</div>
        <div class="hero-pill">◈ Smart Price Insights</div>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 5. PLATFORM INFORMATION
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">Market Coverage</div>
        <div class="info-value">Chennai</div>
        <div class="info-description">Chennai real estate estimation</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">Technology</div>
        <div class="info-value">Machine Learning</div>
        <div class="info-description">Data-driven property valuation</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">Platform</div>
        <div class="info-value">CasaMetric</div>
        <div class="info-description">Intelligent property insights</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 6. PROPERTY FORM HEADING
# =========================================================

st.markdown("""
<div class="section-label">PROPERTY ESTIMATOR</div>
<div class="section-heading">Calculate Your Property Value</div>
<div class="section-description">
    Enter the property information below to receive your estimated valuation.
</div>
""", unsafe_allow_html=True)


# =========================================================
# 7. PROPERTY INPUT FORM
# =========================================================

with st.form("property_form"):

    # BASIC DETAILS

    st.markdown("### 📍 Property Details")

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

    st.markdown("### 📐 Area & Measurements")

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

    st.markdown("### 🏢 Building Specifications")

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
        [
            "Furnished",
            "Semi-Furnished",
            "Unfurnished"
        ]
    )

    st.divider()

    # AMENITIES

    st.markdown("### ✨ Property Amenities")

    c1, c2, c3 = st.columns(3)

    with c1:
        parking = st.selectbox(
            "🚗 Parking",
            [0, 1],
            format_func=lambda x:
                "Available" if x == 1 else "Not Available"
        )

    with c2:
        lift = st.selectbox(
            "🛗 Lift",
            [0, 1],
            format_func=lambda x:
                "Available" if x == 1 else "Not Available"
        )

    with c3:
        gated = st.selectbox(
            "🔐 Gated Community",
            [0, 1],
            format_func=lambda x:
                "Yes" if x == 1 else "No"
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
        "✦  Calculate Property Valuation"
    )


# =========================================================
# 8. MACHINE LEARNING PREDICTION
# =========================================================

if predict_button:

    # INPUT VALIDATION

    if carpet_area > super_area:

        st.error(
            "Carpet area cannot be greater than super area."
        )

    elif floor_number > total_floors:

        st.error(
            "Floor number cannot exceed total floors."
        )

    else:

        # EXACT SAME 16 FEATURES AS YOUR EXISTING MODEL

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

            # PREDICT USING EXISTING TRAINED MODEL

            prediction = float(
                model.predict(input_data)[0]
            )

            if not pd.notna(prediction) or prediction < 0:

                st.error(
                    "The model returned an invalid property price."
                )

            else:

                # CALCULATE PRICE PER SQ FT

                price_per_sqft = (
                    prediction * 100000 / super_area
                )

                # MAIN RESULT

                st.markdown(f"""
                <div class="result-card">

                    <div class="result-eyebrow">
                        YOUR PROPERTY VALUATION
                    </div>

                    <div class="result-price">
                        ₹ {prediction:,.2f} Lakhs
                    </div>

                    <div class="result-subtitle">
                        Estimated property value for your Chennai property
                    </div>

                </div>
                """, unsafe_allow_html=True)

                # RESULT METRICS

                st.markdown("""
                <div class="section-label">
                    VALUATION INSIGHTS
                </div>
                <div class="section-heading">
                    Your Property at a Glance
                </div>
                """, unsafe_allow_html=True)

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.markdown(f"""
                    <div class="result-metric">
                        <div class="result-metric-label">
                            Estimated Price
                        </div>
                        <div class="result-metric-value">
                            ₹{prediction:,.2f} L
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with c2:
                    st.markdown(f"""
                    <div class="result-metric">
                        <div class="result-metric-label">
                            Price per Sq. Ft.
                        </div>
                        <div class="result-metric-value">
                            ₹{price_per_sqft:,.0f}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with c3:
                    st.markdown(f"""
                    <div class="result-metric">
                        <div class="result-metric-label">
                            Property Area
                        </div>
                        <div class="result-metric-value">
                            {super_area:,.0f} sq. ft.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # PROPERTY OVERVIEW

                st.markdown(f"""
                <div class="overview-card">

                    <div class="overview-title">
                        🏡 Property Overview
                    </div>

                    <div class="overview-item">
                        <b>Property Type:</b> {property_type}
                    </div>

                    <div class="overview-item">
                        <b>Locality Category:</b> {locality_type}
                    </div>

                    <div class="overview-item">
                        <b>Bedrooms:</b> {bhk} BHK
                    </div>

                    <div class="overview-item">
                        <b>Bathrooms:</b> {bathrooms}
                    </div>

                    <div class="overview-item">
                        <b>Furnishing:</b> {furnishing}
                    </div>

                    <div class="overview-item">
                        <b>Property Age:</b> {age} years
                    </div>

                    <div class="overview-item">
                        <b>Parking:</b> {"Available" if parking else "Not Available"}
                    </div>

                    <div class="overview-item">
                        <b>Lift:</b> {"Available" if lift else "Not Available"}
                    </div>

                    <div class="overview-item">
                        <b>Gated Community:</b> {"Yes" if gated else "No"}
                    </div>

                    <div class="overview-item">
                        <b>Distance to Metro:</b> {metro_distance} km
                    </div>

                    <div class="overview-item">
                        <b>Distance to City Center:</b> {center_distance} km
                    </div>

                </div>
                """, unsafe_allow_html=True)

                st.success(
                    "Your property valuation has been completed successfully!"
                )

                st.info(
                    "Disclaimer: This is a machine-learning-based estimate. "
                    "It is not an official market valuation or a guaranteed "
                    "selling price."
                )

        except Exception as e:

            st.error(
                f"Prediction failed: {e}"
            )


# =========================================================
# 9. FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <div class="footer-brand">
        CASAMETRIC
    </div>

    <div class="footer-text">
        INTELLIGENT PROPERTY VALUATION · CHENNAI
    </div>

    <div class="footer-text">
        Developed using Python, Streamlit and Machine Learning
    </div>

    <div class="footer-text">
        © 2026 CasaMetric. All rights reserved.
    </div>

</div>
""", unsafe_allow_html=True)
