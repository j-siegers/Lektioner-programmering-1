import requests
import json

url = 'https://restcountries.com/v3.1/name/'
val = input('Välj ett land > ')
valt_land = requests.get(url + val)
valt_land_dict = json.loads(valt_land.text)


for key in valt_land_dict[0]:
    print(key, ':', valt_land_dict[0][key])


