ui_width = 17
num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0

with open('numbers.csv', 'r') as f:
    for file in f:
        file_open = int(file.strip())
        if file_open == 0:
            num_0 += 1
        elif file_open == 1:
            num_1 += 1
        elif file_open == 2:
            num_2 += 1
        elif file_open == 3:
            num_3 += 1
        elif file_open == 4:
            num_4 += 1
        elif file_open == 5:
            num_5 += 1
        elif file_open == 6:
            num_6 += 1
        elif file_open == 7:
            num_7 += 1
        elif file_open == 8:
            num_8 += 1
        elif file_open == 9:
            num_9 += 1
print('-' * ui_width)
print('- NUMANALYZER -'.center(ui_width))
print('-' * ui_width)
print(f'| 0 | {num_0}')
print(f'| 1 | {num_1}')
print(f'| 2 | {num_2}')
print(f'| 3 | {num_3}')
print(f'| 4 | {num_4}')
print(f'| 5 | {num_5}')
print(f'| 6 | {num_6}')
print(f'| 7 | {num_7}')
print(f'| 8 | {num_8}')
print(f'| 9 | {num_9}')
