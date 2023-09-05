todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
search = input('Sök efter en todo: ')
if search in todos:
    print(search, 'finns i listan!')
else:
    print(search, 'finns inte i listan.')
    val = input('Vill du lägga till denna? (j/n) ')
    if val.lower() == 'j':
        todos.append(search)
        print('Todo tillagd!')

print(todos)
