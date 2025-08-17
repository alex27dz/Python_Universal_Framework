import requests

url = "https://api.example.com/users"
headers = {
    "Authorization": "Bearer your_token",
    "Content-Type": "application/json"
}
payload = {
    "name": "Alex",
    "email": "alex@example.com"
}

response = requests.post(url, json=payload, headers=headers)

# Status Code
print(response.status_code)

# JSON Body
print(response.json())
