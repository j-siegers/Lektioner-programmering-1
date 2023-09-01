land = input('Vänligen skriv namnet på ett land: ')
norden = ('danmark' , 'finland', 'island', 'norge', 'sverige')
storBritanien = ('england', 'nordirland', 'skottland', 'wales')
land_liten = land.lower()
if land_liten in norden:
    print(land_liten,'Tillhör norden.')
elif land_liten in storBritanien:
    print(land_liten,'Tillhör Storbritanien.')
else:
    print('Landet du skrev finns inte i min databas!')
    
