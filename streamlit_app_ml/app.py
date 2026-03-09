import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("Iris Flower Prediction App")

sepal_length = st.number_input("SepalLength")
sepal_width = st.number_input("SepalWidth")
petal_length = st.number_input("PetalLength")
petal_width = st.number_input("PetalWidth")

if st.button("Predict"):

    prediction = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

    st.success(f"Predicted Flower: {prediction[0]}")