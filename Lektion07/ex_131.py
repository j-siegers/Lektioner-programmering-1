import requests
import json
integer = input('Ange ett positivt heltal > ')
url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=' + integer
numbers = requests.get(url)
numbers_dict = json.loads(numbers.text)

even_nr = 'är ett jämt nummer.'
try:
    if not numbers_dict['even']:
        even_nr = 'är inte ett jämt nummer.'

    primtal = 'Numret är ett primtal.'
    if not numbers_dict['prime']:
        primtal = 'Numret är inte ett primtal.'

    print(integer, even_nr, primtal)
except KeyError:
    print('Error: Integer can not be less than 2')
    exit()

# Längden på listan med faktorer
lengh = len(numbers_dict['factors'])
# Om det är fler faktorer än 1
if lengh > 1:
    print('Numrets faktorer är ', end='')
    i = 0
    while i < lengh - 1:
        print(numbers_dict['factors'][i], end=', ')
        i += 1
    print('\b\b och', numbers_dict['factors'][-1], '\b.')
# Körs vid 1 faktor
else:
    print('Numrets faktor är', numbers_dict['factors'][0])
