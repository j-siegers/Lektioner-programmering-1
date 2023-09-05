import os
print('Hallå')
if os.name == 'nt':
    os.system('cls')
    print('Du kör Win')
elif os.name == 'posix':
    os.system('clear')
    print('Du kör Mac/Unix')
print('Hej då')

