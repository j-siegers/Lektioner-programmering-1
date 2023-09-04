import random
p = random.random()
print(p)
if p < 0.21:
  print('Du vann något!')
else:
  print('Ingen vinst.')
'''
vokaler = ['a','A','e','E','i','I','o','O','u','U','y','Y','å','Å','ä','Ä','ö','Ö']
sträng = input('Skriv ett ord: ')
ant_vokaler = 0
#tips: för att se om ett tecken är en vokal skriv t.ex.:
#if tecken in vokaler:
for i, tecken in enumerate(sträng):
    if tecken in vokaler:
        ant_vokaler += 1
print('Strängen innehåller', ant_vokaler, 'vokaler')
'''
färger = ['blå', 'svart', 'gul', 'röd', 'violett', 'grön', 'orange', 'grå', 'vit']
print(len(färger))
while True:
  start = input('Vill du få en färg? (j/n) ')
  if start == 'j':
    rand = random.randint(0, (len(färger)-1))
    print(färger[rand])
  else:
    print('Hejdå')
    break

