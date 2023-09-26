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
while True:
    print(ui_widh * '-')
    print('| ', 'Nation'.ljust(13), '| W | D | L | GF | GA |')
    print(ui_widh * '-')

    print('| Brazil'.ljust(16), '|', teams['Brazil']['wins'], '|', teams['Brazil']['draws'], '|',
          teams['Brazil']['losses'],
          '|', teams['Brazil']['goals for'], ' |', teams['Brazil']['goals against'], ' |')

    print('| Serbia'.ljust(16), '|', teams['Serbia']['wins'], '|', teams['Serbia']['draws'], '|',
          teams['Serbia']['losses'],
          '|', teams['Serbia']['goals for'], ' |', teams['Serbia']['goals against'], ' |')

    print('| Switzerland'.ljust(16), '|', teams['Switzerland']['wins'], '|', teams['Switzerland']['draws'], '|',
          teams['Switzerland']['losses'], '|', teams['Switzerland']['goals for'], ' |',
          teams['Switzerland']['goals against'], ' |')

    print('| Costa Rica'.ljust(16), '|', teams['Costa Rica']['wins'], '|', teams['Costa Rica']['draws'], '|',
          teams['Costa Rica']['losses'], '|', teams['Costa Rica']['goals for'], ' |',
          teams['Costa Rica']['goals against'], ' |')
    print(ui_widh * '-')
    val = input('Skriv 1 för att lägga till data.\nSkriv exit för att avsluta\n > ')
    if val == '1':
        user_input = input("Ange spelinformation (Hemmalag, mål, bortalag, mål): ")
        parts = user_input.split(', ')

        # Kontrollera om det finns tillräckligt med delar
        if len(parts) == 4:
            home_team = parts[0]
            home_score = int(parts[1])
            away_team = parts[2]
            away_score = int(parts[3])

            # Anropa add_game-funktionen med de delade värdena
            add_game(home_team, home_score, away_team, away_score)
        else:
            print("Felaktig inmatning. Du måste ange hemmalag, mål, bortalag och mål på en rad.")
            input('Tryck enter för att fortsätta')
    elif val == 'exit':
        exit()

