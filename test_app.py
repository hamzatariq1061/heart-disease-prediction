
import streamlit as st
import joblib
import os

st.title("Heart Disease Model Loading Test")

model_path = "heart_disease_model.pkl"

# Check model file
if os.path.exists(model_path):
    st.success("Model file found!")
    st.write("Model size:", os.path.getsize(model_path), "bytes")

    try:
        package = joblib.load(model_path)

        st.success("Model loaded successfully!")

        st.write("Package keys:", list(package.keys()))
        st.write("Features:", package["features"])
        st.write("Model type:", type(package["model"]).__name__)

    except Exception as e:
        st.error("Model loading failed!")
        st.exception(e)

else:
    st.error("Model file not found!")
