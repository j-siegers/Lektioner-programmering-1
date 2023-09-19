import random

numbers = []
for x in range(10):
    numbers.append(random.randint(0, 20))
print('Before sorting')
for nonsorted in numbers:
    print(f'- {nonsorted}')

print('After sorting')
numbers = sorted(numbers)
for sorted_ in numbers:
    print(f'- {sorted_}')
