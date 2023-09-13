import requests
import json

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
artist = requests.get(url)
artists_dict = json.loads(artist.text)
print('--- Artist DB ---')
for i in artists_dict['artists']:
    print(i['name'])
print('-----------------')
print('Select artist:')
select = input('> ')
print('-----------------')
for i in artists_dict['artists']:
    if select == i['name']:
        artist_id = i['id']  # Artist id tas fram och skickas med URL
        artist_info = requests.get(url + artist_id)
        artists_dict = json.loads(artist_info.text)  # Utökad artist info sparas här

        print(artists_dict['artist']['name'])
        print('*****************')

        print('Genres: ', end='')
        for info in artists_dict['artist']['genres']:
            print(info, end=', ')
        print('\b\b ')

        print('Years active: ', end='')
        for year in artists_dict['artist']['years_active']:
            print(year, end=', ')
        print('\b\b ')

        print('Members: ', end='')
        for member in artists_dict['artist']['members']:
            print(member, end=', ')
        print('\b\b ')
        print('-----------------')


