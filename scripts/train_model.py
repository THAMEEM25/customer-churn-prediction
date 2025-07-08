import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load cleaned dataset
df = pd.read_csv("data/clean_telco.csv")

# Features & target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train best model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Random Forest Accuracy: {round(acc * 100, 2)}%")

# Save final model
with open("models/churn_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Final model saved to models/churn_model.pkl")
