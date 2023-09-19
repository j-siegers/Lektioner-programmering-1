group_b = [
    {
        'country': 'Russia',
        'points': 3
    },
    {
        'country': 'Brazil',
        'points': 7
    },
    {
        'country': 'Cameroon',
        'points': 1
    },
    {
        'country': 'Sweden',
        'points': 5
    }
]


def get_points(element):
    return element['points']


standings = sorted(group_b, key=get_points, reverse=True)
print('Country P')
print('------------')
for team in standings:
    print(team['country'].ljust(10), team['points'])
