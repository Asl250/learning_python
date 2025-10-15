# age = int(input('gimme age: '))
#
# while age < 0:
#     print('gimme correct age')
#     age = int(input('gimme age: '))
#
# print(f'ur {age} years old')

# food = input('enter a food u like (q for quit): ')
#
# while not food == 'q' and not food == 'Q':
#     print(f'u like {food}')
#     food = input('enter another food u like (q for quit): ')
# print('bye')

num = int(input('gimme number between 1 to 10: '))

while num < 1 or num > 10:
    print(f'{num} is not valid ')
    num = int(input('gimme number between 1 to 10: '))
print(f'your number is {num}')