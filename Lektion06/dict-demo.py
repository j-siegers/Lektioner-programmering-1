vehicle = {}
while True:
    car_brand = input('Car brand > ')
    if car_brand == 'exit':
        break
    elif car_brand not in vehicle:
        vehicle[car_brand] = 0

    vehicle[car_brand] += 1

    print('------------')
    print(f'You have seen {vehicle[car_brand]} {car_brand}')
    print('------------')

for x in vehicle:
    print(x, vehicle[x])
