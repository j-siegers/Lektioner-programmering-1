ui_width = 27
print('.: MATHLETE v2.0 :.')
print('-' * ui_width)
tal_lista =[]
while True:
    try:
        tal = input('> ')
        if tal == 'exit':
            break
        tal = int(tal)
        tal_lista.append(tal)

        print('-' * ui_width)
        print('Kardinalitet:'.ljust(15), len(tal_lista))
        print('Summa:'.ljust(15), sum(tal_lista))
        print('Medelvärde:'.ljust(15), sum(tal_lista)/len(tal_lista))

    except:
        print('FEL: Ogiltigt nummer')