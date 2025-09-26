import math

# result = math.sqrt(9)
# result = math.ceil(3.1) #floating number + 1
#result = math.floor(3.1) #floating number - 1

# print(result)



# radios = float(input('gimme radios: '))
# pi = math.pi
# circumference = pi * 2 * radios
#
# print(f'circumference of circle is {round(circumference, 2)}')


# radios = float(input('gimme radios: '))
# pi = math.pi
# area = pow(radios, 2) * pi
# print(round(area, 2))


a = float(input('gimme a number: '))
b = float(input('gimme b number: '))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(round(hypotenuse, 2))