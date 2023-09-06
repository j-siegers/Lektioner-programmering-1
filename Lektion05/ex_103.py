import os
import time
ui_width = 21
while True:
    os.system('cls')
    print('.: PEOPLES DATABASE :.'.center(ui_width))
    print('-' * ui_width)
    print('get_id\t | Get person by ID')
    print('scan_f\t| List people by FORENAME')
    print('scan_s\t| List people by SURNAME')
    print('exit\t| Exit program')
    print('-' * ui_width)
    # *** Menyvalsfunktion ***
    val = input('| > ')

    # *** Sökning på ID nummer ***
    if val.lower() == 'get_id':
        print('-' * ui_width)
        id_no = str(input('| ID = '))
        print('-' * ui_width)
        my_list = [" ̶", "\\", "|", "/"]
        for i in range(5):
            print(f"\r{my_list[0]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[1]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[2]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[3]}", end="")
            time.sleep(0.2)
        print('\n')
        print('-' * ui_width)
        with open('database.csv', 'r', encoding="utf-8") as f:
            for person in f:
                person_list = person.strip().split(",")
                if id_no == person_list[0]:
                    print('| ID:'.ljust(15), person_list[0])
                    print('| FORENAME:'.ljust(15), person_list[1])
                    print('| SURNAME:'.ljust(15), person_list[2])
                    print('| GENDER:'.ljust(15), person_list[3])
                    print('| YEAR:'.ljust(15), person_list[4])

    # *** Sökning på förnamn ***
    elif val.lower() == 'scan_f':
        print('-' * ui_width)
        forename = input('| FORENAME = ')
        print('-' * ui_width)
        my_list = [" ̶", "\\", "|", "/"]
        for i in range(5):
            print(f"\r{my_list[0]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[1]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[2]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[3]}", end="")
            time.sleep(0.2)
        print('\n')
        print('-' * ui_width)
        with open('database.csv', 'r', encoding="utf-8") as f:
            for person in f:
                person_list = person.strip().split(",")
                if forename.lower() == person_list[1].lower():
                    person_ny = ', '.join(person_list)
                    print(person_ny)

    # *** Sökning på efternamn ***
    elif val.lower() == 'scan_s':
        print('-' * ui_width)
        surname = input('| SURNAME = ')
        print('-' * ui_width)
        my_list = [" ̶", "\\", "|", "/"]
        for i in range(5):
            print(f"\r{my_list[0]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[1]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[2]}", end="")
            time.sleep(0.2)
            print(f"\r{my_list[3]}", end="")
            time.sleep(0.2)
        print('\n')
        print('-' * ui_width)
        with open('database.csv', 'r', encoding="utf-8") as f:
            for person in f:
                person_list = person.strip().split(",")
                if surname.lower() == person_list[2].lower():
                    person_ny = ', '.join(person_list)
                    print(person_ny)

    elif val.lower() == 'exit':
        break

    print('-' * ui_width)
    input('| Press Enter to continue...')
    print('''
    
    ''')
