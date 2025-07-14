# scripts/train_model.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

# 📥 Load cleaned dataset
df = pd.read_csv("data/clean_telco.csv")

# ✅ Final selected features based on importance
selected_features = [
    'TotalCharges', 'MonthlyCharges', 'tenure',
    'InternetService_Fiber optic', 'PaymentMethod_Electronic check',
    'Contract_Two year', 'gender_Male', 'PaperlessBilling_Yes',
    'OnlineSecurity_Yes', 'Partner_Yes', 'TechSupport_Yes',
    'SeniorCitizen'
]

X = df[selected_features]
y = df['Churn']

# 🧪 Handle imbalance using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# 🔍 Hyperparameter tuning for Random Forest
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid.fit(X_resampled, y_resampled)
best_model = grid.best_estimator_

# 🔀 Train/test split for final evaluation
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# 🎯 Train final model
model = RandomForestClassifier(**best_model.get_params())
model.fit(X_train, y_train)

# 📈 Evaluate on test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Final Random Forest Accuracy (on test set): {accuracy * 100:.2f}%")

# 💾 Save model
with open("models/churn_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Final model saved to models/churn_model.pkl")

# 📊 Show top feature importances
importances = model.feature_importances_
features = X.columns
feature_importance = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)

print("🔝 Top Important Features:")
for feature, score in feature_importance:
    print(f"{feature}: {score:.4f}")
