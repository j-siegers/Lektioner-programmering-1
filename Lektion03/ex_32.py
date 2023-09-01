namn = input('Ange ditt namn: ')
ålder = int(input('Ange din ålder: '))
print('-----')

if ålder == 1:
    sömn = 14
elif ålder == 2:
    sömn = 13
elif ålder == 3:
    sömn = 12
elif ålder == 4:
    sömn = 11.5
elif ålder == 5 or 6:
    sömn = 11
elif ålder == 7:
    sömn = 10.5
elif ålder == 8 or 9 or 10:
    sömn = 10
elif ålder == 11:
    sömn = 9.5
elif ålder == 12 or 13 or 14 or 15:
    sömn = 9
elif ålder == 16:
    sömn = 8.5
elif ålder >= 17:
    sömn = 8

print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, ') sova minst ', sömn, 'timmar per natt.')
