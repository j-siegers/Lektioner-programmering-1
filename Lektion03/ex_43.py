import random
slumpTal = random.randint(0, 99)
anvTal = -1
räknare = 0
print('.:    THE HIGHER LOWER GAME    :.')
print('---------------------------------')
print('Welcome to The Higher Lower game.')
print('I will randomise a number between')
print('0 and 99. \nCan you guess it?')
print('---------------------------------')

while slumpTal != anvTal:
    anvTal = int(input('Your guess > '))
    räknare += 1
    if anvTal < slumpTal:
        print('HIGHER!')
    elif anvTal > slumpTal:
        print('LOWER!')

print('---------------------------------')
print(anvTal,'is correct! \nIt took you',räknare,'guesses. \nGood job!')
