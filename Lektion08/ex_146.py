def print_table(result: list):
    counter = 1
    print('-' * 52)
    print('| # |', 'Nation'.ljust(13), '| W | D | L | GF | GA | GD | P |')
    print('-' * 52)
    for team in result:
        print('|', counter, '|', team['country'].ljust(13), '|', team['wins'], '|', team['draws'], '|',
              team['losses'], '|', team['goals for'], ' |', team['goals against'], ' |',
              team['goals for'] - team['goals against'], ' |', team['wins'] * 3 + team['draws'], '|')
        counter += 1
    print('-' * 52)


team_list = [
    {'wins': 2, 'draws': 1, 'losses': 0, 'goals for': 5, 'goals against': 1, 'country': 'Brazil'},
    {'wins': 1, 'draws': 0, 'losses': 2, 'goals for': 2, 'goals against': 4, 'country': 'Serbia'},
    {'wins': 1, 'draws': 2, 'losses': 0, 'goals for': 5, 'goals against': 4, 'country': 'Switzerland'},
    {'wins': 0, 'draws': 1, 'losses': 2, 'goals for': 2, 'goals against': 5, 'country': 'Costa Rica'}
]

print_table(team_list)
