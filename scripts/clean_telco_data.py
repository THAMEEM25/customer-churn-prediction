import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Drop customerID
df.drop("customerID", axis=1, inplace=True)

# Convert Churn column to binary
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Drop rows with missing TotalCharges (converted from blanks)
df.dropna(inplace=True)

# One-hot encode categorical columns
categorical_cols = df.select_dtypes(include="object").columns.tolist()
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Save the cleaned dataset
df.to_csv("data/clean_telco.csv", index=False)

print("✅ Data cleaned and saved as 'clean_telco.csv'")
