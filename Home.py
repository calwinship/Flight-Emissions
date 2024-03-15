import streamlit as st
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

# Streamlit app title
st.title('Flight Emission Calculator')

st.write("This app calculates the CO2 emissions of a flight based on the flight details provided. The flight must be in the future.")

# Form for flight details
with st.form("flight_info"):
    origin = st.text_input("Origin airport code (e.g., JFK):")
    destination = st.text_input("Destination airport code (e.g., LHR):")
    carrier_code = st.text_input("Carrier code (e.g., AA):")
    flight_number = st.number_input("Flight number:", min_value=1, value=100, format="%d")
    year = st.number_input

    year = st.number_input("Year:", min_value=2024, max_value=2100, value=2024, format="%d")
    month = st.number_input("Month:", min_value=1, max_value=12, value=1, format="%d")
    day = st.number_input("Day:", min_value=1, max_value=31, value=1, format="%d")

    submit_button = st.form_submit_button("Calculate Emissions")

if submit_button:
    # Preparing the request data
    flight_data = {
        "flights": [
            {
                "origin": origin,
                "destination": destination,
                "operatingCarrierCode": carrier_code,
                "flightNumber": int(flight_number),
                "departureDate": {
                    "year": int(year),
                    "month": int(month),
                    "day": int(day)
                }
            }
        ]
    }



    # API endpoint
    url = f"https://travelimpactmodel.googleapis.com/v1/flights:computeFlightEmissions?key={api_key}"
    
    # Replace YOUR_API_KEY with your actual API key
# key=API_KEY

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=flight_data, headers=headers)
    
    response_data = response.json()

    # if 'flightEmissions' in response_data:
    #     for flight in enumerate(response_data['flightEmissions'], start=1):
    #         emissions = flight['emissionsGramsPerPax']
    #         st.subheader(f'Flight {i} Emissions (grams per passenger):')
    #         st.write(f"- First class: {emissions['first']}")
    #         st.write(f"- Business class: {emissions['business']}")
    #         st.write(f"- Premium economy class: {emissions['premiumEconomy']}")
    #         st.write(f"- Economy class: {emissions['economy']}")
    # else:
    #     st.error("No flight emissions data found.")




    if 'flightEmissions' in response_data:
        emissions = response_data['flightEmissions'][0]['emissionsGramsPerPax']
        classes = ['First', 'Business', 'Premium Economy', 'Economy']
        values = [emissions['first'], emissions['business'], emissions['premiumEconomy'], emissions['economy']]

        fig, ax = plt.subplots()
        ax.bar(classes, values)
        ax.set_ylabel('Emissions (grams per passenger)')
        ax.set_title('Flight Emissions by Class')

        st.pyplot(fig)
    else:
        st.error("No flight emissions data found.")


