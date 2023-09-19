def km_to_miles(dist):
    km = dist.split()
    return float(km[0]) * 0.62137


def miles_to_km(dist):
    miles = dist.split()
    return float(miles[0]) / 0.62137


distance = input('Ange distans > ')
if 'km' in distance:
    distance_converted = km_to_miles(distance)
    print(f'{distance} motsvarar {distance_converted} miles.')

elif 'miles' in distance:
    distance_converted = miles_to_km(distance)
    print(f'{distance} motsvarar {distance_converted} km.')

else:
    print('Välj km eller miles')
