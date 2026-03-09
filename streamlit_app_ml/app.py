import streamlit as st
import pickle
import os

# Get current directory of app.py
current_dir = os.path.dirname(__file__)

# Build full path to model
model_path = os.path.join(current_dir, "model.pkl")

# Load model
with open(model_path, "rb") as file:
    model = pickle.load(file)

st.title("Iris Flower Prediction App")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):

    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    st.success(f"Predicted Flower: {prediction[0]}")
