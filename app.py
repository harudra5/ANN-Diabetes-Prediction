import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load the saved model
model = load_model("diabetes_ann_model.keras")

# Load the preprocessor
preprocessor = joblib.load("preprocessor.pkl")

st.title("Diabetes Risk Prediction using ANN")

st.header("Enter Patient Details")

# ---------------- Row 1 ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    year = st.number_input("Year", 2000, 2100, 2022)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])

with col3:
    age = st.number_input("Age", 0, 120, 30)

with col4:
    location = st.selectbox("Location", ["Urban", "Rural"])


# ---------------- Row 2 ----------------
col1, col2, col3 = st.columns(3)

with col1:
    race = st.selectbox(
    "Race",
    ["AfricanAmerican", "Asian", "Caucasian", "Hispanic", "Other"]
)

with col2:
    hypertension = st.selectbox(
        "Hypertension",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with col3:
    heart_disease = st.selectbox(
        "Heart Disease",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# ---------------- Row 3 ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    smoking_history = st.selectbox(
        "Smoking History",
        ["never", "No Info", "current", "former", "ever"]
    )

with col2:
    bmi = st.number_input("BMI", 10.0, 70.0, 25.0)

with col3:
    hbA1c_level = st.number_input("HbA1c Level", 3.0, 15.0, 5.5)

with col4:
    blood_glucose_level = st.number_input(
        "Blood Glucose Level",
        50,
        400,
        120
    )


input_data = pd.DataFrame({
    "year": [year],
    "gender": [gender],
    "age": [age],
    "location": [location],

    "race:AfricanAmerican": [1 if race == "AfricanAmerican" else 0],
    "race:Asian": [1 if race == "Asian" else 0],
    "race:Caucasian": [1 if race == "Caucasian" else 0],
    "race:Hispanic": [1 if race == "Hispanic" else 0],
    "race:Other": [1 if race == "Other" else 0],

    "hypertension": [hypertension],
    "heart_disease": [heart_disease],
    "smoking_history": [smoking_history],
    "bmi": [bmi],
    "hbA1c_level": [hbA1c_level],
    "blood_glucose_level": [blood_glucose_level]
})[
    [
        "year",
        "gender",
        "age",
        "location",
        "race:AfricanAmerican",
        "race:Asian",
        "race:Caucasian",
        "race:Hispanic",
        "race:Other",
        "hypertension",
        "heart_disease",
        "smoking_history",
        "bmi",
        "hbA1c_level",
        "blood_glucose_level",
    ]
]

if st.button("Predict"):

    processed_data = preprocessor.transform(input_data)

    prediction = model.predict(processed_data)

    probability = prediction[0][0]

    st.write(f"Prediction Probability: {probability:.4f}")
    st.write(f"Diabetes Risk: {probability * 100:.2f}%")

    if probability >= 0.5:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")