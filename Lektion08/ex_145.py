def make_list(teams_dict: dict):
    tmp_list = []
    tmp_dict = {}
    for key in teams_dict:
        tmp_dict = teams_dict[key]
        tmp_dict['country'] = key
        tmp_list.append(tmp_dict)
    return tmp_list


teams = {
    'Brazil': {
        'wins': 2,
        'draws': 1,
        'losses': 0,
        'goals for': 5,
        'goals against': 1
    },
    'Serbia': {
        'wins': 1,
        'draws': 0,
        'losses': 2,
        'goals for': 2,
        'goals against': 3
    },
    'Switzerland': {
        'wins': 1,
        'draws': 2,
        'losses': 0,
        'goals for': 5,
        'goals against': 4
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 1,
        'losses': 2,
        'goals for': 2,
        'goals against': 5
    }
}

team_list = make_list(teams)

print(team_list)
