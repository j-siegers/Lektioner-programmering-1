import json

# attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']

with open('data.json') as fName:
    data = json.loads(fName.read())
print(data[3])
