import time
import json
import os

if os.path.exists('notes.json'):
    with open('notes.json') as f:
        notebook = json.loads(f.read())
else:
    with open('notes.json', 'x') as f:
        notebook = {}

while True:
    print('.:  ALWAYSNOTES  :.')
    print('-- gold edition --')
    print('******************')

    try:
        for note in notebook:
            print(f'- {note}')
        print('--------------')
        print('view'.ljust(6), '| view note')
        print('add'.ljust(6), '| add note')
        print('rm'.ljust(6), '| remove note')
        print('exit'.ljust(6), '| exit program')
        print('--------------')
        choice = input('meny > ').lower()
        if choice == 'view':
            view = input('Write a note title > ')
            print('--------------')
            print(f'{notebook[view]}')
            print('--------------')

        elif choice == 'add':
            print('--------------')
            add_title = input('Write a title > ')
            add_text = input('Write a text > ')
            print('--------------')
            notebook[add_title] = add_text
            print('Note added')
            print('--------------')

        elif choice == 'rm':
            print('--------------')
            remove = input('Title to remove > ')
            del notebook[remove]
            print('--------------')
            print('Note deleted')
            print('--------------')

        elif choice == 'exit':
            print('Saving to notes.json', end='')
            #  Save indicator animation
            for i in range(10):
                print('.', end='')
                time.sleep(0.5)
            print('\n')
            with open('notes.json', 'w') as f:
                f.write(json.dumps(notebook))
            break
        else:
            print('The menu choice does not exist')
        input('Press enter to continue...')

    except:
        print('Error: Unknown note!')
