# 📊 Customer Churn Prediction Using Machine Learning

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. This project predicts whether a customer is likely to discontinue the service based on customer demographics, subscription details, and service usage.

The project applies machine learning techniques to analyze customer behavior and helps businesses identify customers who are at risk of leaving so that appropriate retention strategies can be implemented.

---

## 🎯 Objective

To build a machine learning model that predicts customer churn using historical telecom customer data.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains information about customers such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Tech Support
- Streaming Services
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn (Target Variable)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 📊 Project Workflow

### 1. Data Collection
- Loaded the Telco Customer Churn dataset using Pandas.

### 2. Data Exploration (EDA)
- Analyzed customer demographics.
- Visualized churn distribution.
- Studied contract types and churn.
- Analyzed monthly charges and tenure.
- Created correlation heatmaps.

### 3. Data Cleaning
- Removed unnecessary columns.
- Converted TotalCharges to numeric.
- Handled missing values.
- Encoded categorical variables.

### 4. Data Preprocessing
- Performed One-Hot Encoding.
- Split dataset into training and testing data.
- Standardized numerical features using StandardScaler.

### 5. Model Building
Implemented two machine learning algorithms:

- Logistic Regression
- Random Forest Classifier

### 6. Model Evaluation
Evaluated models using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

### 7. Feature Importance
Identified important factors influencing customer churn.

### 8. Deployment
Developed a simple interactive Streamlit web application to predict customer churn.

---

## 📈 Features

- Customer Churn Prediction
- Exploratory Data Analysis
- Machine Learning Classification
- Data Visualization
- Streamlit Web Interface
- Model Persistence using Joblib

---

## 📁 Project Structure

```
Customer-Churn-Prediction
│
├── app.py
├── churn_project.ipynb
├── README.md
├── requirements.txt
│
├── data
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
└── models
    ├── churn_model.pkl
    ├── scaler.pkl
    └── columns.pkl
```

---

## 🚀 Future Enhancements

- Deploy the application on Streamlit Cloud
- Improve model accuracy using XGBoost
- Add SHAP Explainability
- Build an interactive dashboard
- Add customer retention recommendations

---

## 👩‍💻 Author

**Yashaswini N P**

Information Science & Engineering

Machine Learning | Data Analytics | Python
