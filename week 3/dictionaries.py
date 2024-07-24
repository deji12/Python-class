human = {
    "name": "John",
    "age": 20,
    "gender": "male",
    "height": 5.9,
    "children": [
        {
            "name": "Jane",
            "age": 12,
            "gender": "female",
            "height": 5.5,
        },
        {
            "name": "Abby",
            "age": 10,
            "gender": "female",
            "height": 5.1,
        }
    ],
    "married": True
}

print(human["children"][1]["gender"])

# Accessing a value by its key
print(human["children"])
human["name"] = "Taiwo"

print(human)