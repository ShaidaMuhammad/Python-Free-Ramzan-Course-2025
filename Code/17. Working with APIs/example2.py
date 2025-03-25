import requests

try:  
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

print("Completed.")
