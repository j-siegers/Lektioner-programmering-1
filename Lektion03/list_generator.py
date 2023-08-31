print('Choose a starting number, ending number, and increment to use')
start_no = int(input('Start at: '))
end_no = int(input('End before: '))
increment_no = int(input('Increment between values: '))

for counter in range(start_no, end_no, increment_no):
    print(counter)