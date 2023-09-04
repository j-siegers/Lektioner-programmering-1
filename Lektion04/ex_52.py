ui_width = 27
print('*' * ui_width)
print('* The Great Divider *'.center(ui_width))
print('-' * ui_width)
print('\nBeräknar c för uttrycket:')
print(('-' * ui_width))

try:
    tal_a = input('a = ')
    tal_b = input('b = ')
    tal_a = float(tal_a)
    tal_b = float(tal_b)
    if tal_a == 0 or tal_b == 0:
        print('-' * ui_width)
        print('FEL: Division med 0')
    print('-' * ui_width)
    print(tal_a, '/', tal_b, '=', tal_a / tal_b)
except:
    print('FEL: ogiltigt nummer')
    print('-' * ui_width)


