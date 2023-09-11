notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
print('Ta bort artikel:')
titel = input('\ttitel > ')

del notes[titel]
for note in notes:
    print('----')
    print(f'Titel: {note} \nText: {notes[note]}')

