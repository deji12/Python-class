import requests

# get post put patch delete

rates = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/aud.json")
data = rates.json()

for i in data["aud"]:
    print(f"Currency: {i} Rate: {data['aud'][i]}")