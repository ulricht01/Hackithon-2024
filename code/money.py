import requests
import json
def fetch_expenditure_data(url):
    response = requests.get(url)
    data = response.json()
    return data

data = requests.get('https://zpravy.udhpsh.cz/zpravy/k2020.json').json()

# Initialize a dictionary to store the expenditure data for each party
expenditure_data = {}

# Extract URLs for expenditure files and fetch the data
for party in data["parties"]:
    party_name = party["shortName"]
    for file in party["files"]:
        if file["subject"] == "vydaje":  # Check if the subject is "vydaje" (expenditure)
            expenditure_url = file["url"]
            try:
                expenditure_data[party_name] = fetch_expenditure_data(expenditure_url)
            except Exception as e:
                expenditure_data[party_name] = f"Error fetching data: {e}"

# Print the expenditure data for each party
for party, data in expenditure_data.items():
    print(f"Expenditure data for {party}:")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    print("\n")