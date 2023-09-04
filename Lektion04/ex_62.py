print('Robber Translate'.center(20))
print('-' * 20)
konsonanter = 'bcdfghjklmnpqrstvwxz'
text = input('Svenska \t< ')
text_ny = []
for index, bokstav in enumerate(text):
    text_ny.append(text[index])
    if bokstav in konsonanter:
        text_ny.pop()  # Tar bort bokstav och ersätter den sedan med nästa rad.
        text_ny.append(text[index]+'o'+text[index])
text_str = ''.join(text_ny)
print('Rövarspråk \t> ', text_str)
