todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
ta_bort = int(input('Ta bort todo (index): '))
try:
    del todos[ta_bort]
except:
    print('Indexet existerar inte')
print(todos)

