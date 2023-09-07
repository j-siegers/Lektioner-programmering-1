import json
import os
ui_width = 19

if os.path.exists('heltal.json'):
    # Öppna en befintlig fil
    with open('heltal.json') as f_name:
        num_list = json.loads(f_name.read())
        if type(num_list) == int:  # Om filen skulle innehålla int
            digit_list = [int(digit) for digit in str(num_list)]  # Gör om till list
            num_list = list(digit_list)

else:
    # Skapa en ny fil
    with open('heltal.json', 'x') as f_name:
        num_list = []
while True:
    os.system('cls')
    summa = 0  # Nollställer summeringen efter varje ny inmatat tal
    print('.: intMEMORIZER :.')
    print('*' * ui_width)
    if len(num_list) > 0:
        for nummer in num_list:
            print('*', + nummer)
            summa += nummer
        print('-' * ui_width)
    print(f'SUMMA :\t{summa}')
    print('-' * ui_width)
    print('\tMata in heltal')
    print('0\tStänger scriptet')
    print('-' * ui_width)
    try:
        inmatning = int(input('> '))
        if inmatning != 0:
            if inmatning not in num_list:
                num_list.append(inmatning)
        else:
            with open('heltal.json', 'w') as f_name:
                f_name.write(json.dumps(num_list))

            os.system('cls')
            print('''
            Programmet stängdes!
            
            Strax innan programmet stängdes
            så skrevs följande sträng till
            textfilen heltal.json:
            ''')
            print(f'"{num_list}"'.center(ui_width))
            print('''
            Nästa gång du kör programmet
            kommer heltal.json läsas in på
            nytt.        
            ''')
            break
    except ValueError:
        print('Du matade in ett felaktigt värde!')
        input('Tryck Enter för att fortsätta')

    os.system('cls')
