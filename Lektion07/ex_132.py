import json
import requests
ui_width = 31
print('Enter the name of the city\nfor which you want forecasts:')
city = input('> ')
print('-' * ui_width)
response = requests.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city)
response_dictionary = json.loads(response.text)
if 'error' not in response_dictionary:
    print('FORECASTS'.center(31))
    print('*' * ui_width)
    forecast = response_dictionary['forecasts']

    for i in forecast:
        print(i['date'].ljust(14), i['forecast'].rjust(15))
else:
    print(response_dictionary['error'])
