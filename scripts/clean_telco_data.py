import pandas as pd

# Load original dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Drop customerID
df.drop("customerID", axis=1, inplace=True)

# Remove rows with blank TotalCharges
df = df[df["TotalCharges"].str.strip() != ""]

# Convert TotalCharges to float
df["TotalCharges"] = df["TotalCharges"].astype(float)

# ✅ Final 12 selected readable features
selected_features = [
    'TotalCharges', 'MonthlyCharges', 'tenure',
    'InternetService', 'PaymentMethod', 'Contract',
    'gender', 'PaperlessBilling', 'OnlineSecurity',
    'Partner', 'TechSupport', 'SeniorCitizen', 'Churn'
]

# Keep only those columns
df = df[selected_features]

# Save clean readable version
df.to_csv("data/clean_telco_readable.csv", index=False)