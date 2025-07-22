import streamlit as st
import pandas as pd
import pickle

# Page config
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

# Load pipeline
with open("models/final_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

# CSS for minimal radio styling (optional)
st.markdown("""
<style>
label[data-testid="stRadio"] > div[role="radiogroup"] > label {
    background-color: #121212;
    color: #ffffff;
    border: 1px solid #444;
    border-radius: 12px;
    padding: 8px 16px;
    margin: 5px;
    transition: all 0.3s ease;
}
label[data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
    background-color: #1f1f1f;
    border-color: #6c63ff;
}
label[data-testid="stRadio"] > div[role="radiogroup"] > label[data-selected="true"] {
    background-color: #6c63ff;
    color: white;
    border-color: #6c63ff;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Customer Churn Predictor")
st.write("Provide customer details below to predict churn.")

# Layout: 3 main columns
col1, col2, col3 = st.columns(3)

# Personal Info
with col1:
    st.subheader(" Personal Info")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["Yes", "No"])
    partner = st.selectbox("Partner", ["Yes", "No"])

# Services
with col2:
    st.subheader(" Services")
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

# Billing Info
with col3:
    st.subheader(" Billing Info")
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Charges + Tenure: 2-column layout for better alignment
col4, col5 = st.columns(2)
with col4:
    monthly_charges = st.slider("Monthly Charges", min_value=18.0, max_value=120.0, value=70.0)
with col5:
    total_charges = st.slider("Total Charges", min_value=0.0, max_value=9000.0, value=1000.0)

tenure = st.slider("Tenure (in months)", 0, 72, 12)

# Predict Button
if st.button("Predict Churn"):

    # Create input
    input_df = pd.DataFrame([{
        'TotalCharges': total_charges,
        'MonthlyCharges': monthly_charges,
        'tenure': tenure,
        'InternetService': internet,
        'PaymentMethod': payment,
        'Contract': contract,
        'gender': gender,
        'PaperlessBilling': paperless,
        'OnlineSecurity': online_security,
        'Partner': partner,
        'TechSupport': tech_support,
        'SeniorCitizen': 1 if senior == "Yes" else 0
    }])

    # Predict using full pipeline
    prediction = pipeline.predict(input_df)[0]

    # Show result
    if prediction == 1:
        st.error(" Customer is **likely to churn**.")
    else:
        st.success(" Customer is **likely to stay**.")
