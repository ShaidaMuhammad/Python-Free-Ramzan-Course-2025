import json

data = {
    "name": "Khan",
    "age": 30,
    "city": "Charsadda"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
