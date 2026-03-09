import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Marks Dashboard")

data = pd.read_csv("data.csv")

st.write("Dataset Preview")
st.write(data)

st.subheader("Bar Chart")

fig, ax = plt.subplots()
ax.bar(data["Name"], data["Marks"])
st.pyplot(fig)