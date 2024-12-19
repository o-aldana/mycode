import requests
import json

# Define the URL for the open-notify API
url = "http://api.open-notify.org/astros.json"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Define the filename to save the data
    filename = "astros.json"

    # Write the JSON data into a file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"JSON data successfully written to {filename}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}") 
