import random


def get_even(lista):
    even_l = []
    for number in lista:
        if not number % 2:
            even_l.append(number)
    return even_l


numbers = []
for x in range(10):
    numbers.append(random.randint(0,9))

even = get_even(numbers)
print('Even:', even)
print('Numbers:', numbers)

