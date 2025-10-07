# Python calculator

# operator = input('gimme operator (+ - * /): ')
# num1 = float(input('gimme your 1st number: '))
# num2 = float(input('gimme your 2st number: '))
#
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-' :
#     print(num1 - num2)
# elif operator == '*':
#     print(num1 * num2)
# elif operator == '/':
#     print(num1 / num2)
# else:
#     print('give real operator')


# weight convertor

# weight = int(input('gimme weight: '))
# unit = input('gimme unit (K/L): ')
#
# if unit == 'K':
#     weight = weight * 2.205
#     print(f'{round(weight, 2)} LBS')
# elif unit == 'L' :
#     weight = weight / 2.205
#     print(f'{round(weight, 2)} KGs')
# else:
#     print(f'{unit} is not valid')

# temperature conversation
unit = input('is temperature in Celsius or Fahrenheit (C/F): ')
temp = float(input('gimme temperature: '))

if unit == 'C' :
    temp = (temp * 9 / 5) + 32
    print(f'temperature is {round(temp, 1)}K')
elif unit == 'F':
    temp = (temp - 32) /9 *5
    print(f'temperature is {round(temp, 1   )}C')
else:
    print(f'{unit} is not valid')