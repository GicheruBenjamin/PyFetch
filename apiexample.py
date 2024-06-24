import requests

api_url = "https://randomuser.me/api/"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    user = data["results"][0]
    print(f"Name: {user['name']['first']} {user['name']['last']}")
else:
    print(f"Error: {response.status_code}")