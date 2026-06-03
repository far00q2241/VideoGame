import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('vgsales_model.pkl')

st.title("Video Game Global Sales Prediction")

rank = st.number_input("Rank", min_value=1)
year = st.number_input("Year", min_value=1980, max_value=2025)

na_sales = st.number_input("NA Sales")
eu_sales = st.number_input("EU Sales")
jp_sales = st.number_input("JP Sales")
other_sales = st.number_input("Other Sales")

name_freq = st.number_input("Name Frequency")
platform_freq = st.number_input("Platform Frequency")
genre_freq = st.number_input("Genre Frequency")
publisher_freq = st.number_input("Publisher Frequency")

if st.button("Predict"):

    data = pd.DataFrame({
        'Rank':[rank],
        'Year':[year],
        'NA_Sales':[na_sales],
        'EU_Sales':[eu_sales],
        'JP_Sales':[jp_sales],
        'Other_Sales':[other_sales],
        'Publisher_freq':[publisher_freq],
        'Name_freq':[name_freq],
        'Platform_freq':[platform_freq],
        'Genre_freq':[genre_freq]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Global Sales: {prediction[0]:.2f}") 


    