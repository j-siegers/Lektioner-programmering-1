ui_width = 35
bilar = ['Mercedes', 'Volvo', 'Toyota']
while True:
    print('.: STACKMASTER V1.33.7 :.'.center(ui_width))
    print('-' * ui_width)
    for bil in bilar:
        print(f'- {bil}')
    print('-' * ui_width)
    print('| MENU |'.center(ui_width))
    print('-' * ui_width)
    print('push\t| Push element to stack')
    print('pull\t| Pull element to stack')
    print('exit\t| Exit program')
    print('-' * ui_width)
    val = input(' MENU > ')
    if val.lower() == 'push':
        bilar.append(input('Add a car: > '))
    elif val.lower() == 'pull':
        try:
            bilar.pop()
        except IndexError:
            print('The list is already empty!')
            print(input())
    elif val.lower() == 'exit':
        break

