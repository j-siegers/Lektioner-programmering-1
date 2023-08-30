import math
print('.: Korvkollen 1.0.1 :.')
print('----------------------')
print('Hur många elever vill ha...')

vanl_korvar_x2 = int(input('2 vanliga korvar > '))
vanl_korvar_x3= int(input('3 vanliga korvar >'))
veg_korvar_x2 = int(input('2 veganska korvar'))
veg_korvar_x3 = int(input('3 veganska korvar'))
print('----------------------')
print('-    INKÖPSLISTA     -')
print('----------------------')
vanl_korvar = vanl_korvar_x2 * 2 + vanl_korvar_x3 * 3
print(math.ceil(vanl_korvar/8))
print('| Vanlig korv: ')