import random


myList = ["Deji", 56.9, [1, 4, 7], {"name": "Taiwo"}]

random_item = random.choice(myList)

print(random_item)

import requests

response = requests.get('https://catfact.ninja/fact')
print(response.json())


