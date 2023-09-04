text = input('Ange en text: ')
bokstav = input('Ange en bokstav: ')
i = 0
count = 0
while i < len(text):
    if text[i] == bokstav:
        count += 1
    i += 1
print('Bokstaven', bokstav, 'förekommer', count, 'gånger i texten')
