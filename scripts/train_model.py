import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

# 📥 Load the clean readable dataset
df = pd.read_csv("data/clean_telco_readable.csv")

# ✅ List of final selected features (readable form)
selected_features = [
    'TotalCharges', 'MonthlyCharges', 'tenure',
    'InternetService', 'PaymentMethod',
    'Contract', 'gender', 'PaperlessBilling',
    'OnlineSecurity', 'Partner', 'TechSupport',
    'SeniorCitizen'
]

X = df[selected_features]
y = df['Churn']

# 🔄 Encode categorical columns
label_encoders = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Encode target
y = LabelEncoder().fit_transform(y)

# ⚖️ Handle imbalance with SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# 🔀 Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)

# 🔧 Grid Search for best Random Forest
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

# 📈 Evaluate best model
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Final Random Forest Accuracy (on test set): {accuracy * 100:.2f}%")

# 💾 Save final model
with open("models/churn_model.pkl", "wb") as f:
    pickle.dump(best_model, f)
print("✅ Final model saved to models/churn_model.pkl")

# 🔍 Show feature importance
importances = best_model.feature_importances_
for feature, score in sorted(zip(X.columns, importances), key=lambda x: x[1], reverse=True):
    print(f"{feature}: {score:.4f}")
