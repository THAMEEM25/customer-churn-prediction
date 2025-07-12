import streamlit as st
import pickle

# Load trained model
with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# 🌌 Custom page styling
st.set_page_config(page_title="Churn Predictor", layout="wide")
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .title-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 0 25px #00ffe0;
        text-align: center;
        margin-bottom: 30px;
    }
    .predict-box {
        background-color: #101010;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 0 15px #00ffe0;
        text-align: center;
        font-size: 1.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔷 Glowing Title
st.markdown('<div class="title-box"><h1>Customer Churn Prediction</h1></div>', unsafe_allow_html=True)

# 🔢 Input Form
st.subheader("Enter Customer Details:")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (in months)", 0, 72, 24)
    monthly_charges = st.slider("Monthly Charges", 18, 120, 65)
    total_charges = st.slider("Total Charges", 0, 9000, 2500)
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    paperless_billing = st.radio("Paperless Billing", ["Yes", "No"])
    online_security = st.radio("Online Security", ["Yes", "No"])
    partner = st.radio("Has a Partner", ["Yes", "No"])
    tech_support = st.radio("Tech Support Enabled", ["Yes", "No"])
    senior_citizen = st.radio("Senior Citizen", ["Yes", "No"])

# ✅ Prediction logic
if st.button("Predict Churn"):
    features = [
        total_charges,
        monthly_charges,
        tenure,
        1 if internet_service == "Fiber optic" else 0,
        1 if payment_method == "Electronic check" else 0,
        1 if contract_type == "Two year" else 0,
        1 if gender == "Male" else 0,
        1 if paperless_billing == "Yes" else 0,
        1 if online_security == "Yes" else 0,
        1 if partner == "Yes" else 0,
        1 if tech_support == "Yes" else 0,
        1 if senior_citizen == "Yes" else 0,
    ]
    prediction = model.predict([features])[0]

    result_text = "⚠️ The customer is likely to CHURN." if prediction == 1 else "✅ The customer is likely to STAY."
    st.markdown(f'<div class="predict-box">{result_text}</div>', unsafe_allow_html=True)
