notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
while True:
    try:
        anteckning = input('Anteckning > ')
        if anteckning == 'exit':
            break
        print('-----')
        print(notes[anteckning])
        print('-----')

    except KeyError:
        print('FEL: anteckningen finns inte')
