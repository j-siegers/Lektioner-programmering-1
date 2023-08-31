ålder = int(input('Hur gammal är du? '))
if ålder < 18:
    print('Du är myndig inom', 18-ålder , 'år')
else:
    print('Du är redan myndig')
