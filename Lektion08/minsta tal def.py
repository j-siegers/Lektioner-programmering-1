numbers = [5, 2, 7, 4, 9, 2.1, 1.99]


def minimum(lista):
    minsta_tal = lista[0]
    for i in lista:
        if minsta_tal > i:
            minsta_tal = i
    return minsta_tal


minsta_tal = minimum(numbers)
print(minsta_tal)

