import random
dice = random.randint(1, 6)

d1 = '''
---------
| X     |
|       |
|       |
---------
'''
d2 = '''
---------
| X     |
|       |
|     X |
---------
'''
d3 = '''
---------
| X     |
|   X   |
|     X |
---------
'''
d4 = '''
---------
| X   X |
|       |
| X   X |
---------
'''
d5 = '''
---------
| X   X |
|   X   |
| X   X |
---------
'''
d6 = '''
---------
| X X X |
| X X X |
| X X X |
---------
'''
print('Du slog en', dice,':a')
if dice == 1:
    print(d1)
elif dice == 2:
    print(d2)
elif dice == 3:
    print(d3)
elif dice == 4:
    print(d4)
elif dice == 5:
    print(d5)
elif dice == 6:
    print(d6)