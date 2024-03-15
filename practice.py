import requests 
	# 18 Mar 2024	New York (JFK)	London (LHR)	77W
flight_data = {
    "flights": [
        {
            "origin": "JFK",
            "destination": "LHR",
            "operatingCarrierCode": "AA",
            "flightNumber": 100,
            "departureDate": {
                "year": 2024,
                "month": 3,
                "day": 18
            }
        }
    ]
}



url = "https://travelimpactmodel.googleapis.com/v1/flights:computeFlightEmissions?key=AIzaSyD7N-5WoOw18POQIXewMmBW7wedVptiAas"
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=flight_data, headers=headers)
# print("Response:", response.json())

response_data = response.json()

for flight in response_data['flightEmissions']:
        emissions = flight['emissionsGramsPerPax']
        print(f"- First class: {emissions['first']}")
        print(f"- Business class: {emissions['business']}")
        print(f"- Premium economy class: {emissions['premiumEconomy']}")
        print(f"- Economy class: {emissions['economy']}")

# Response: {'flightEmissions': [
#     {'flight': 
#         {'origin': 'JFK', 
#         'destination': 'LHR', 
#         'operatingCarrierCode': 'AA', 
#         'flightNumber': 100, 
#         'departureDate': {'year': 2024, 'month': 3, 'day': 18}
#         }, 
#       'emissionsGramsPerPax': 
#         {'first': 2906060, 'business': 2324848, 'premiumEconomy': 871817, 'economy': 581212}}], 
#         'modelVersion': {'major': 1, 'minor': 9, 'patch': 0, 'dated': '20240314'}}