import pandas as pd
import pickle

# Load trained model
with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load structure of cleaned dataset
df = pd.read_csv("data/clean_telco.csv")
X = df.drop("Churn", axis=1)

# Start with a valid row as a template
new_customer = X.iloc[0:1].copy()

# User inputs
tenure = float(input("Enter tenure (e.g., 12): "))
monthly_charges = float(input("Enter MonthlyCharges (e.g., 75.5): "))
total_charges = float(input("Enter TotalCharges (e.g., 850): "))

# Update values
new_customer["tenure"] = tenure
new_customer["MonthlyCharges"] = monthly_charges
new_customer["TotalCharges"] = total_charges

# Predict churn
prediction = model.predict(new_customer)

# Output result
if prediction[0] == 1:
    print("\n⚠️  The customer is likely to CHURN.")
else:
    print("\n✅ The customer is likely to STAY.")
