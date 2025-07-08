![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Made with](https://img.shields.io/badge/Made%20with-Python-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

This project is a machine learning-based system that predicts whether a telecom customer is likely to **churn (leave)** or **stay**, based on their usage data. It includes a clean interactive web interface using Streamlit and well-organized Python scripts for training and prediction.

---

## 🖥️ Demo

> 📸 Local App Preview  
> (No online deployment — built for internship portfolio)

![App Screenshot]("C:\Users\THAMEEM ANSAR\OneDrive\Pictures\Screenshots\Screenshot 2025-07-08 122344.png")
---

## 🚀 Features

- 🔍 Predicts customer churn using ML models (Random Forest, Logistic Regression, etc.)
- 📈 Compares multiple algorithms and selects the best-performing one
- 🧹 Cleaned dataset with EDA performed
- 🌐 Streamlit web app with sliders and glowing dark UI
- 📂 Ready-to-use GitHub project structure for internship portfolio

---

## 📁 Project Structure

<pre><code>## 📁 Project Structure ``` Customer Churn Analysis/ ├── data/ ├── models/ ├── scripts/ ├── dashboard/ ├── notebooks/ ├── README.md ├── requirements.txt └── .gitignore ``` </code></pre>

---

## 💻 How to Run

### 1. Train the Model
   
```bash
python scripts/train_model.py

### 2. Predict in Terminal
  
python scripts/predict_churn.py

### 3. Run the Web App

streamlit run dashboard/app.py

---
## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt

---
---

## 📁 Notes

- `.gitignore` is used to keep the project clean by skipping:
  - Python cache files
  - Virtual environments
  - Unwanted system files
  - Model files (optional)


## 🙋‍♂️ Author

**Mohamed Thameem Ansar**  
*Data Analyst*