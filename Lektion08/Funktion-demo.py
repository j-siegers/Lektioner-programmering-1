import random


def random_card():
    kortlek = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    slumpat_kort = random.choice(kortlek)
    return slumpat_kort


while True:
    print(random_card())
    val = input('Spela igen? (j/n) ')
    if val == 'n':
        break
