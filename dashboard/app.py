import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

# CSS for dark techy background and glowing title
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        color: white;
    }
    .title-box {
        background-color: #222;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 20px #00f0ff;
        margin-bottom: 30px;
    }
    .title-box h1 {
        color: #00f0ff;
        font-size: 40px;
        font-family: monospace;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Glowing title
st.markdown('<div class="title-box"><h1>Customer Churn Prediction</h1></div>', unsafe_allow_html=True)

# Input form
st.subheader("📋 Enter Customer Details")

TotalCharges = st.slider("Total Charges (₹)", min_value=0.0, max_value=10000.0, value=500.0)
MonthlyCharges = st.slider("Monthly Charges (₹)", min_value=0.0, max_value=200.0, value=70.0)
tenure = st.slider("Tenure (months)", min_value=0, max_value=72, value=12)

InternetService = st.selectbox("Internet Service Type", ["Fiber optic", "Other"])
InternetService_Fiber_optic = 1 if InternetService == "Fiber optic" else 0

PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Other"])
PaymentMethod_Electronic_check = 1 if PaymentMethod == "Electronic check" else 0

Contract = st.selectbox("Contract Type", ["Two year", "Other"])
Contract_Two_year = 1 if Contract == "Two year" else 0

gender = st.selectbox("Gender", ["Male", "Female"])
gender_Male = 1 if gender == "Male" else 0

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaperlessBilling_Yes = 1 if PaperlessBilling == "Yes" else 0

OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
OnlineSecurity_Yes = 1 if OnlineSecurity == "Yes" else 0

Partner = st.selectbox("Has Partner?", ["Yes", "No"])
Partner_Yes = 1 if Partner == "Yes" else 0

TechSupport = st.selectbox("Tech Support", ["Yes", "No"])
TechSupport_Yes = 1 if TechSupport == "Yes" else 0

SeniorCitizen = st.selectbox("Senior Citizen?", ["Yes", "No"])
SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0

# Predict button
if st.button("Predict Churn"):
    input_data = np.array([
        TotalCharges, MonthlyCharges, tenure,
        InternetService_Fiber_optic, PaymentMethod_Electronic_check,
        Contract_Two_year, gender_Male, PaperlessBilling_Yes,
        OnlineSecurity_Yes, Partner_Yes, TechSupport_Yes,
        SeniorCitizen
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("❌ The customer is likely to CHURN.")
    else:
        st.success("✅ The customer is likely to STAY.")
