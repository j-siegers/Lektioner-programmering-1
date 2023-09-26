from random import randint


class Rectangle:
    def __init__(self, length, width):
        if length > 0:
            self.__length = length
        else:
            print('Felaktig längd. Längd måste vara större än 0.')

        if width > 0:
            self.__width = width
        else:
            print('Felaktig bredd. Bredden måste vara större än 0.')

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print('Felaktig längd. Längd måste vara större än 0.')

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print('Felaktig bredd. Bredden måste vara större än 0.')

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def omkrets(self):
        return self.__width * 2 + self.__length * 2

    def area(self):
        return self.__width * self.__length


r_list = []
area = 0
for i in range(1000):
    r_list.append(Rectangle(randint(1, 10), randint(1, 10)))

for n in r_list:
    area += Rectangle.area(n)

print(area)

