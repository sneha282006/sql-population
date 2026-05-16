import streamlit as st
import pandas as pd

df = pd.read_csv("population.csv")

st.title("Population Dashboard")

st.write(df)

gender_count = df["GENDER"].value_counts()

st.subheader("Gender Distribution")
st.write(gender_count)

st.bar_chart(gender_count)

st.subheader("Age Distribution")
st.bar_chart(df["age"])
