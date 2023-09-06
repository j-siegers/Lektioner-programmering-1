with open('fil.txt', 'r') as f:
    MinVariabel = f.read()
while True:
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
    if menyVal.lower() == 'exit':
        break
'''


with open('fil .txt', 'w') as f :
    MinVariabel = f.write()
print(MinVariabel)
'''