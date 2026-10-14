
import streamlit as st
import sys
import importlib.metadata as metadata

st.title("Heart Disease Dependency Test")

st.write("Python Version:", sys.version)

packages = [
    "streamlit",
    "pandas",
    "scikit-learn",
    "joblib"
]

for package in packages:
    try:
        version = metadata.version(package)
        st.success(f"{package}: Installed ({version})")
    except metadata.PackageNotFoundError:
        st.error(f"{package}: NOT INSTALLED")
