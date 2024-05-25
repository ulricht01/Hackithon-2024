import requests
import json
import pandas as pd
import os

def fetch_expenditure_data(url):
    response = requests.get(url)
    data = response.json()
    return data
def get_parties(url):
    response = requests.get(url)
    data = response.json()
    return data
# Fetch the main JSON data
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

parties = {}

# Normalize and concatenate all expenditure data into a single DataFrame
all_dataframes = []

for party, data in expenditure_data.items():
    if isinstance(data, list):  # Ensure the data is a list of dictionaries
        df = pd.json_normalize(data)
        df['party'] = party  # Add a column for the party name
        all_dataframes.append(df)
    else:
        print(f"Skipping data for {party} due to error: {data}")

# Concatenate all DataFrames into one
if all_dataframes:
    final_df = pd.concat(all_dataframes, ignore_index=True)
    print(final_df)
else:
    print("No valid data to concatenate.")

final_df.to_csv('code/datafiles/expenditure_data.csv', sep=";", index=False)