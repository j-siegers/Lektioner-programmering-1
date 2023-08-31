while True:
    tal1 = int(input('Ange ett tal: '))
    tal2 = int(input('Ange ännu ett tal: '))
    tal3 = int(input('Ange ett sista tal: '))

    if tal1 > tal2:
        if tal1 > tal3:
            print('Det största inmatade talet är',tal1)
        else:
            print('Det största inmatade talet är',tal3)
    elif tal2 > tal3:
            print('Det största inmatade talet är',tal2)
    else:
            print('Det största inmatade talet är',tal3)
    switch = input('En gång till? (j/n) ')
    if switch == 'n':
         print('Tack och hej!')
         break
    

     

        
