kön = input('Ange kön: ')
hårfärg = input('Ange hårfärg: ')
ögonfärg = input('Ange ögonfärg: ')

celeb = [
{
'namn': 'Daniel Radcliffe',
'kön': 'man',
'hårfärg': 'brun',
'ögonfärg': 'brun'
},
{
'namn': 'Rupert Grint',
'kön': 'man',
'hårfärg': 'röd',
'ögonfärg': 'blå'
},
{
'namn': 'Emma Watson',
'kön': 'kvinna',
'hårfärg': 'brun',
'ögonfärg': 'brun'
},
{
'namn': 'Selena Gomez',
'kön': 'kvinna',
'hårfärg': 'brun',
'ögonfärg': 'brun'
},
{
'namn': 'Bruce Willis',
'kön': 'man',
'hårfärg': 'svart',
'ögonfärg': 'brun'
},
{
'namn': 'Clint Eastwood',
'kön': 'man',
'hårfärg': 'grå',
'ögonfärg': 'brun'
},
{
'namn': 'Sean Connery',
'kön': 'man',
'hårfärg': 'grå',
'ögonfärg': 'brun'
},
{
'namn': 'Sean Penn',
'kön': 'man',
'hårfärg': 'brun',
'ögonfärg': 'grön'
},
{
'namn': 'Alicia Vikander',
'kön': 'kvinna',
'hårfärg': 'brun',
'ögonfärg': 'brun'
},
{
'namn': 'Will Smith',
'kön': 'man',
'hårfärg': 'svart',
'ögonfärg': 'brun'
}
]
result = None
resultat = []
for i in celeb:
    if i['kön'] == kön and i['hårfärg'] == hårfärg and i['ögonfärg'] == ögonfärg:
       result = i['namn']
       resultat.append(result)
resultat_str = ' och '.join(resultat)       
if result == None:
    print('Ingen matchning hittades') 
else:
    print(resultat_str)
