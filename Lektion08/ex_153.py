def add_game(home_team: str, home_score: int, away_team: str, away_score: int):
    global teams
    # Lagring av vinster, förluster och lika poäng
    if home_score > away_score:
        teams[home_team]['wins'] += 1
        teams[away_team]['losses'] += 1
    elif away_score > home_score:
        teams[away_team]['wins'] += 1
        teams[home_team]['losses'] += 1
    else:
        teams[away_team]['draws'] += 1
        teams[home_team]['draws'] += 1
    # Lagring av totalt antal mål
    teams[home_team]['goals for'] += home_score
    teams[away_team]['goals for'] += away_score
    # Lagring av totalt antal insläppta mål
    teams[home_team]['goals against'] += away_score
    teams[away_team]['goals against'] += home_score


def make_list(teams_dict: dict):
    tmp_list = []
    tmp_dict = {}
    for key in teams_dict:
        tmp_dict = teams_dict[key]
        tmp_dict['country'] = key
        tmp_list.append(tmp_dict)
    return tmp_list


def sort_list(lista):
    lista.sort(key=lambda points: points['wins'] * 3 + points['draws'], reverse=True)
    return lista


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


ui_widh = 40

teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    }
}

add_game('Costa Rica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)
add_game('Brazil', 2, 'Costa Rica', 0)
add_game('Serbia', 1, 'Switzerland', 2)
add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'Costa Rica', 2)

teams_list = make_list(teams)
teams_list_sorted = sort_list(teams_list)
print_table(teams_list_sorted)
