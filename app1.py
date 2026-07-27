import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")

st.title("📊 Customer Churn Prediction")

st.sidebar.header("Customer Details")

gender = st.sidebar.selectbox("Gender", ["Male","Female"])
senior = st.sidebar.selectbox("Senior Citizen",[0,1])
partner = st.sidebar.selectbox("Partner",["Yes","No"])
dependents = st.sidebar.selectbox("Dependents",["Yes","No"])
phone = st.sidebar.selectbox("Phone Service",["Yes","No"])
multiple = st.sidebar.selectbox("Multiple Lines",["No","Yes","No phone service"])
internet = st.sidebar.selectbox("Internet Service",["DSL","Fiber optic","No"])
online_sec = st.sidebar.selectbox("Online Security",["Yes","No","No internet service"])
online_backup = st.sidebar.selectbox("Online Backup",["Yes","No","No internet service"])
device = st.sidebar.selectbox("Device Protection",["Yes","No","No internet service"])
tech = st.sidebar.selectbox("Tech Support",["Yes","No","No internet service"])
tv = st.sidebar.selectbox("Streaming TV",["Yes","No","No internet service"])
movies = st.sidebar.selectbox("Streaming Movies",["Yes","No","No internet service"])
contract = st.sidebar.selectbox("Contract",["Month-to-month","One year","Two year"])
paperless = st.sidebar.selectbox("Paperless Billing",["Yes","No"])
payment = st.sidebar.selectbox("Payment Method",
["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])

tenure = st.sidebar.slider("Tenure",0,72,12)
monthly = st.sidebar.number_input("Monthly Charges",0.0,500.0,70.0)
total = st.sidebar.number_input("Total Charges",0.0,100000.0,1000.0)

if st.button("Predict Churn"):
    data = {c:0 for c in columns}

    def setcol(name):
        if name in data:
            data[name]=1

    data["SeniorCitizen"]=senior
    data["tenure"]=tenure
    data["MonthlyCharges"]=monthly
    data["TotalCharges"]=total

    if gender=="Male": setcol("gender_Male")
    if partner=="Yes": setcol("Partner_Yes")
    if dependents=="Yes": setcol("Dependents_Yes")
    if phone=="Yes": setcol("PhoneService_Yes")

    if multiple=="Yes": setcol("MultipleLines_Yes")
    elif multiple=="No phone service": setcol("MultipleLines_No phone service")

    if internet=="Fiber optic": setcol("InternetService_Fiber optic")
    elif internet=="No": setcol("InternetService_No")

    mapping={
      "OnlineSecurity":online_sec,
      "OnlineBackup":online_backup,
      "DeviceProtection":device,
      "TechSupport":tech,
      "StreamingTV":tv,
      "StreamingMovies":movies
    }
    for prefix,val in mapping.items():
        if val=="Yes":
            setcol(prefix+"_Yes")
        elif val=="No internet service":
            setcol(prefix+"_No internet service")

    if contract=="One year":
        setcol("Contract_One year")
    elif contract=="Two year":
        setcol("Contract_Two year")

    if paperless=="Yes":
        setcol("PaperlessBilling_Yes")

    if payment=="Credit card (automatic)":
        setcol("PaymentMethod_Credit card (automatic)")
    elif payment=="Electronic check":
        setcol("PaymentMethod_Electronic check")
    elif payment=="Mailed check":
        setcol("PaymentMethod_Mailed check")

    X = pd.DataFrame([data])
    X = X[columns]
    Xs = scaler.transform(X)

    pred = model.predict(Xs)[0]
    prob = model.predict_proba(Xs)[0][1]

    st.subheader("Prediction Result")
    st.metric("Churn Probability", f"{prob*100:.2f}%")

    if pred==1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")
