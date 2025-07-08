import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load data structure
df = pd.read_csv("data/clean_telco.csv")
X = df.drop("Churn", axis=1)
template_input = X.iloc[0:1].copy()

# ---------- Page Config ----------
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; padding: 1rem;">
    <div style="
        background-color: rgba(15, 32, 39, 0.9);
        padding: 1.5rem 2rem 1.2rem 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 20px #00ffd0;
        text-align: center;
        white-space: nowrap;
        line-height: 1.2;
    ">
        <h1 style="color: #00ffd0; margin: 0; font-family: 'Segoe UI', sans-serif; font-size: 2.3rem;">
            📊 Customer Churn Prediction
        </h1>
        <p style="color: white; font-size: 0.85rem; margin: 0.3rem 0 0;">
            Enter customer details and predict churn in real-time 🚀
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Background animation (gradient pulse)
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
    }
    .main {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #0f2027);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 25px #00ffd0;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stSlider > div > div {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Full-page animated background
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100%;
        width: 100%;
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #0f2027);
        background-size: 400% 400%;
        animation: gradientFlow 15s ease infinite;
    }

    @keyframes gradientFlow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main {
        background-color: rgba(0, 0, 0, 0.55);  /* Optional glass effect */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 25px #00ffd0;
    }

    .stSlider > div > div {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sliders -----------
tenure = st.slider("📅 Tenure (months)", 0, 72, 12)
monthly = st.slider("💰 Monthly Charges", 0.0, 150.0, 70.0)
total = st.slider("📦 Total Charges", 0.0, 10000.0, 850.0)

# ---------- Prediction ----------
if st.button("🔮 Predict Churn"):
    template_input["tenure"] = tenure
    template_input["MonthlyCharges"] = monthly
    template_input["TotalCharges"] = total

    prediction = model.predict(template_input)

    st.markdown("---")
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to **CHURN**.")
    else:
        st.success("✅ This customer is likely to **STAY**.")
st.markdown("</div>", unsafe_allow_html=True)
