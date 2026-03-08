import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("groundwater_model.pkl")

st.title("Groundwater Stress Prediction System")

st.write("Enter groundwater parameters to predict stress level")


monsoon = st.number_input("Recharge from rainfall During Monsoon Season (BCM)")
non_monsoon = st.number_input("Recharge from rainfall During Non Monsoon Season (BCM)")
total_recharge = st.number_input("Total Annual Ground Water Recharge (BCM)")
extraction = st.number_input("Total Current Annual Ground Water Extraction (BCM)")
availability = st.number_input("Net Ground Water Availability for future use (BCM)")


if st.button("Predict Groundwater Stress"):

    data = pd.DataFrame({
        'Recharge from rainfall During Monsoon Season':[monsoon],
        'Recharge from rainfall During Non Monsoon Season':[non_monsoon],
        'Total Annual Ground Water Recharge':[total_recharge],
        'Total Current Annual Ground Water Extraction':[extraction],
        'Net Ground Water Availability for future use':[availability]
    })

    prediction = model.predict(data)

    st.write("Model prediction:", prediction[0])

    if prediction[0] == "Safe":
        st.success("Groundwater Status: SAFE")
    else:
        st.error("Groundwater Status: STRESSED")