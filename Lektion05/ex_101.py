import os
if os.path.exists('sign.txt'):
    # Öppna om en befintlig fil finns
    print('')
    f = open('sign.txt', 'a')
else:
    # Skapa annars en ny fil
    f = open('sign.txt', 'x')
f.close()
while True:
    os.system('cls')
    print('''
    
    ''')
    with open('sign.txt', 'r') as f:
        MinVariabel = f.read()
    print('| ' + '-' * 51,'|')
    print('|\t#\t' + '-' * 29,'\t\t#\t\t  |')
    print('|  ###\t|' + MinVariabel.center(27) +'|\t#  ###\t\t  |')
    print('|  ###\t' + '-' * 29, ' ### ###\t\t  |')
    print('|\t|\t\t\t|\t\t\t|\t\t\t|\t|\t\t  |')
    print('| ' + '-' * 51,'|')
    print('|\tC\t|\tChange sign message')
    print('|\tE\t|\tExit program')
    print('|' + '-' * 31)
    menyVal = input('| > ')
    if menyVal.lower() == 'e':
        break
    elif menyVal.lower() == 'c':
        with open('sign.txt', 'w') as f:
            MinVariabel = f.write(input('| Change sign to: > '))

'''


with open('fil .txt', 'w') as f :
    MinVariabel = f.write()
print(MinVariabel)
'''