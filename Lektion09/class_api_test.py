import requests
import json


class Catfact:
    def __init__(self):
        self.height = 2
        self.length = 3
        self.width = None

    def cat_dict(self):
        i = self.width
        response = requests.get('https://meowfacts.herokuapp.com/?count=' + i)
        response_dict = json.loads(response.text)
        self.width = response_dict
        return self.width


print('------------------------')
print('.: CAT FACT GENERATOR :.')
print('------------------------')


cat1 = Catfact()
cat1.width = input('How many cat facts do you want? > ')
cat_dict = Catfact.cat_dict(cat1)
print(cat1.height)
print(cat1.width)

for cat in cat_dict['data']:
    print('*', cat)


