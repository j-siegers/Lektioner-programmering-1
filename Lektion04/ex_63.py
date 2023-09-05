print('*' * 40)
print('Palindromen kontroll V1.0'.center(40))
print('*' * 40)
palindrom = input('Ange sträng: ')
palindrom_bak = ''
i = len(palindrom) - len(palindrom) - len(palindrom) - 1
counter = -1
while i < counter:
    palindrom_bak += palindrom[counter]
    palindrom_bak = palindrom_bak.strip().lower()
    counter -= 1
palindrom_kompakt = palindrom.lower().replace(' ', '')
if palindrom_bak == palindrom_kompakt:
    print('\'', palindrom, '\'', 'är ett palindrom.')

else:
    print('\'', palindrom, '\'', 'är inte ett palindrom.')
