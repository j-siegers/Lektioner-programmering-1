total = 0
for tal in range(1000001):
    total = tal + total
print(f'Summan av alla heltal är {total}')


total = 0
for tal in range(501):
    if tal % 2 == 1:
        total += tal
print(f'Summan av alla udda heltal är {total}')
