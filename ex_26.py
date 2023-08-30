import math
print('.: Korvkollen 1.0.1 :.')
print('----------------------')
print('Hur många elever vill ha...')

vanl_korvar_x2 = int(input('2 vanliga korvar > '))
vanl_korvar_x3= int(input('3 vanliga korvar > '))
veg_korvar_x2 = int(input('2 veganska korvar > '))
veg_korvar_x3 = int(input('3 veganska korvar > '))
print('----------------------')
print('-    INKÖPSLISTA     -')
print('----------------------')
vanl_korvar = math.ceil((vanl_korvar_x2 * 2 + vanl_korvar_x3 * 3)/8)
print('| Vanlig korv:  ',vanl_korvar , 'förpackningar')
veg_korvar = math.ceil((veg_korvar_x2 * 2 + veg_korvar_x3 * 3)/4)
print('| Vegansk korv: ', veg_korvar, 'förpackningar')
dryck = vanl_korvar_x2 + vanl_korvar_x3 + veg_korvar_x2 + veg_korvar_x3
print('| Dryck:        ',dryck, 'drickor')
print('----------------------')
summa = vanl_korvar * 20.95 + veg_korvar * 34.95 + dryck * 13.95
print('|', summa, 'SEK')
print('----------------------')



