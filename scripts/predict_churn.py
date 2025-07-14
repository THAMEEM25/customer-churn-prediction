import pickle

# 🚀 Load trained model
with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

print("🔍 Please enter the following customer details:\n")

# 1. MonthlyCharges
MonthlyCharges = float(input("Monthly Charges (₹): "))

# 2. TotalCharges
TotalCharges = float(input("Total Charges so far (₹): "))

# 3. Tenure
tenure = int(input("Tenure in months (e.g., 12): "))

# 4. InternetService_Fiber optic
internet_service = input("Internet Service Type (Fiber/Other): ").strip().lower()
InternetService_Fiber_optic = 1 if internet_service == "fiber" else 0

# 5. PaymentMethod_Electronic check
payment_method = input("Payment Method (Electronic Check/Other): ").strip().lower()
PaymentMethod_Electronic_check = 1 if payment_method == "electronic check" else 0

# 6. Contract_Two year
contract_type = input("Contract Type (Two year/Other): ").strip().lower()
Contract_Two_year = 1 if contract_type == "two year" else 0

# 7. gender_Male
gender = input("Gender (Male/Female): ").strip().lower()
gender_Male = 1 if gender == "male" else 0

# 8. PaperlessBilling_Yes
paperless = input("Paperless Billing (Yes/No): ").strip().lower()
PaperlessBilling_Yes = 1 if paperless == "yes" else 0

# 9. OnlineSecurity_Yes
online_security = input("Online Security Enabled? (Yes/No): ").strip().lower()
OnlineSecurity_Yes = 1 if online_security == "yes" else 0

# 10. Partner_Yes
partner = input("Do they have a partner? (Yes/No): ").strip().lower()
Partner_Yes = 1 if partner == "yes" else 0

# 11. TechSupport_Yes
tech_support = input("Tech Support Enabled? (Yes/No): ").strip().lower()
TechSupport_Yes = 1 if tech_support == "yes" else 0

# 12. SeniorCitizen
senior = input("Is the customer a Senior Citizen? (Yes/No): ").strip().lower()
SeniorCitizen = 1 if senior == "yes" else 0

# 🧠 Final input in correct order
input_data = [
    TotalCharges,
    MonthlyCharges,
    tenure,
    InternetService_Fiber_optic,
    PaymentMethod_Electronic_check,
    Contract_Two_year,
    gender_Male,
    PaperlessBilling_Yes,
    OnlineSecurity_Yes,
    Partner_Yes,
    TechSupport_Yes,
    SeniorCitizen
]

# 📊 Predict
prediction = model.predict([input_data])[0]

# ✅ Show Result
if prediction == 1:
    print("\n❌ The customer is likely to CHURN.")
else:
    print("\n✅ The customer is likely to STAY.")
