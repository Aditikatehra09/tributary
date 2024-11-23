import requests

# Data to send in the POST request
payload = {"engine_temperature": 0.3}

# Send the POST request to the Flask server
response = requests.post("http://0.0.0.0:8000/record", json=payload)

# Print the response from the server
print(response.status_code)
print(response.json())
