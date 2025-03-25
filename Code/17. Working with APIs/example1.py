import requests

response = requests.get("https://api.github.com/users/ShaidaMuhammad")

print(response.status_code)
# print(response.json())
# print(response.headers)