import requests

data = requests.get("https://randomuser.me/api")

# Check if the connection is successfully established (200 = yes, 404 = no)
print(data.status_code)
# Print the data in a json format
print(data.json())

# Get the user's full name
first_name = data.json()["results"][0]["name"]["first"]
last_name = data.json()["results"][0]["name"]["last"]
print(f"{first_name} {last_name}")
