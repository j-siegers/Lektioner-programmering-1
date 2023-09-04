print('Choose a starting number, ending number, and increment to use')
while True:
    try:    
        start_no = int(input('Start at: '))
        end_no = int(input('End before: '))
        increment_no = int(input('Increment between values: '))
        for counter in range(start_no, end_no, increment_no):
            print(counter)
        break
    except:
        print('Ett fel uppstod!\nFörsök igen? (j/n)')
        val = input('> ')
        val = val.upper()
        if val == 'N':
            break




