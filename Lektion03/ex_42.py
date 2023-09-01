tabell = int(input('Ange multiplikationstabell> '))
x = 1
while True:
    for i in range(x, (x+3)):
        print(tabell * i)
        x += 1
    in_ = input('Fortsätt? (ja/nej) ')
    if in_ == 'nej':
        break