import requests
import json

'''
r = requests.get('https://webservice--mdh.repl.co/')
if r.status_code == 200:
    print(r.text)
    print(r.headers)
    print('\n', r.headers['Content-Type'])
else:
    print('ERROR')
'''

response = requests.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm')
response_dictionary = json.loads(response.text)
print(response_dictionary['city'].capitalize().center(20))
print('---------------------')
forecast = response_dictionary['forecasts']

for i in forecast:
    print(i['date'], i['forecast'])
