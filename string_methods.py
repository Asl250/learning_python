from celery.bin.result import result

# name = input('enter your name: ')

# result = len(name)
# result = name.find('a') # finds first
# result = name.rfind('b') # finds last r - its reverse
# result = name.capitalize() # bob - Bob
# result = name.upper()  # bob - BOB
# result = name.lower() # Bob - bob
#result = name.isdigit() # prints true if in contains ONLY numbers
# result = name.isalpha()
# result = name.count('a')
# result = name.replace('-', '')

# print(result)



username  = input('gimme username: ')


if len(username) > 12 :
    print('it should not be more characters than 12')
elif username.find(' ') >= 1:
    print('it should not contain spaces')
elif not username.isalpha():
    print('username can not contain numbers ')
else:
    print(f'welcome {username}')

