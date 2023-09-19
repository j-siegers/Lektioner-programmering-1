import json
import requests

url = 'http://worldtimeapi.org/api/timezone/'
response = requests.get(url)
response_dictionary = json.loads(response.text)

# Listar alla tillgängliga tidszoner
for i in response_dictionary:
    print(i)

# Skriv in namnet på tidszonen
print('.: Choose a time zone :.')
timezone = input('> ')

# Skickar förfrågan på tidszonen till servern
response = requests.get(url + timezone)
response_dictionary = json.loads(response.text)

# Innehållet från förfrågan skrivs ut
for i in response_dictionary:
    print(i, ':', response_dictionary[i])

