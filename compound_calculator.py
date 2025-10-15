
while True:
    principle = float(input('gimme principle amount: '))
    if principle < 0:
        print('principle can not be under 0')
    else:
        break

while True:
    rate = float(input('gimme rate : '))
    if rate < 0:
        print('rate can not be under 0')
    else:
        break

while True:
    time = float(input('gimme time in years: '))
    if time < 0:
        print('time can not be under 0')
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f'balance is ${total:.2f}')