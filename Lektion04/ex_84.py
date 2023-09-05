todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
ta_bort = (input('Ta bort todo (namn): '))
try:
    todos.remove(ta_bort)
except:
    print('Namnet existerar inte')
print(todos)

