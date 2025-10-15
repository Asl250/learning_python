# for i in range(1, 21):
#     if i == 13:
#         continue
#     else:
#         print(i)

# import time
#
# my_time = int(input('gimme time: '))
#
# for i in range(my_time, 0, -1 ):
#     second = i%60
#     minute = int(i / 60) % 60
#     hour =  int(i/3600) % 24
#     print(f'{hour}:{minute:02}:{second:02}')
#     time.sleep(1)

rows = int(input('gimme row: '))
columns = int(input('gimme column: '))
symbol = input('gimme symbol to use: ')


for i in range(rows):
    for x in range(columns):
        print(symbol, end=' ')
    print()