# DEFAULT ARGUMENTS
# def net_price(list_price, discount = 0.0, tax = 0.05):
#     return list_price * (1-discount) * (1+tax)


# print(net_price(500))
# print(net_price(500, 0.1, 0))


# import time
#
# def count(end, start=0):
#     for i in range(start, end+1):
#         print(i)
#         time.sleep(1)
#     print('Done')
# count(30,10)


# keyword arguments
# def hello(greeting, title, first, last):
#     print(f'{greeting} {title}{first} {last}')
#
# hello('hello', title='MR.', last='Doe', first='John')



# *args == arguments & **kwargs == key arguments

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2, 3, 10))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=' ')
#
# display_name('john', 'doe')


# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} : {value}')
#
# print_address(street='Central',city='London', zip='777111')


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=' ')
#     print()
#
#     print(f"{kwargs.get('street')}")
#
# shipping_label('DR', "John", 'Doe', 'III', street='Central',city='Detroit', zip='111222333')