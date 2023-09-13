import requests
import json
print('------------------------')
print('.: CAT FACT GENERATOR :.')
print('------------------------')
i = str(input('How many cat facts do you want? > '))
response = requests.get('https://meowfacts.herokuapp.com/?count=' + i)
response_dict = json.loads(response.text)
for cat in response_dict['data']:
    print('*', cat)
