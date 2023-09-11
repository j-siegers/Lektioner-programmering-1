notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
print('Lägg till artikel:')
titel = input('\ttitel > ')
text = input('\ttext > ')
notes[titel] = text
for note in notes:
    print('----')
    print(f'Titel: {note} \nText: {notes[note]}')

