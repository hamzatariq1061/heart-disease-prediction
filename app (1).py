
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("heart_disease_model.pkl")

package = load_model()

model = package["model"]
scaler = package["scaler"]
features = package["features"]

st.title("❤️ Heart Disease Prediction System")

st.write(
    "Enter patient information to generate "
    "an educational machine learning prediction."
)

st.info(
    "For academic demonstration only. "
    "This application cannot diagnose or rule out heart disease."
)

age = st.number_input(
    "Patient Age",
    min_value=1,
    max_value=120,
    value=55,
    step=1
)

sex = st.selectbox(
    "Sex",
    options=[1, 0],
    format_func=lambda x: "Male" if x == 1 else "Female"
)

cp = st.selectbox(
    "Chest Pain Type",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Typical Angina",
        2: "Atypical Angina",
        3: "Non-Anginal Pain",
        4: "Asymptomatic"
    }[x]
)

thalach = st.number_input(
    "Maximum Heart Rate Achieved (BPM)",
    min_value=50,
    max_value=250,
    value=140,
    step=1
)

if st.button("Predict Heart Disease"):

    patient = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "thalach": thalach
    }

    input_df = pd.DataFrame(
        [patient],
        columns=features
    )

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.warning(
            "Model Prediction: Heart Disease Present"
        )
    else:
        st.success(
            "Model Prediction: No Heart Disease"
        )

    st.caption(
        "Prediction is based on a limited academic dataset "
        "and must not be used for medical decisions."
    )
