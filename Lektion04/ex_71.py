import os
POST_1 = ''
POST_2 = ''
POST_3 = ''
while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:\t', POST_1)
    print('P2:\t', POST_2)
    print('P3:\t', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')
    val = input('Meny > ').lower()
    if val == 'c':
        c_val = input('Vilken post vill du ändra? (P1 - P2 - P3) > ').lower()
        if c_val == 'p1':
            POST_1 = input('Mata in data och avsluta med Enter > ')
        elif c_val == 'p2':
            POST_2 = input('Mata in data och avsluta med Enter > ')
        elif c_val == 'p3':
            POST_3 = input('Mata in data och avsluta med Enter > ')

    elif val == 'e':
        print('Tack och hej!')
        break
    else:
        print('Välj ett kommando från menyn')
    input('Tryck enter för att fortsätta ...')
    print('''
    
    ''')
