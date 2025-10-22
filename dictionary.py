# capitals = {
#     'USA':'Washington',
#     'India':'Delhi',
#     'China': 'Beijing',
#     'Russia': 'Moscow'
# }
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get('Japan'))
# capitals.update({'Germany': 'Berlin'}) # add element
# capitals.update({'China': 'Tokio'}) # update element
# capitals.pop('China') #delete element
#capitals.popitem() # delete the last element
#capitals.clear() #delete all elements

# keys = capitals.keys()
# values = capitals.values()
# items = capitals.items()

# for key, value in capitals.items():
#     print(f'{key} : {value}')

# print(capitals)



#concession stand game
# menu = {
#     'pizza':5.99,
#     'nachos':1.99,
#     'hotdog':2.99,
#     'burger':2.99,
#     'soda':0.99,
#     'lemonade':1.99,
# }
#
# card = []
# total = 0
#
# print('-----------MENU-----------')
# for key, value in menu.items():
#     print(f'{key:10}: ${value:.2f}')
#
# print('-------------------------')
#
# while True :
#     food = input('select an item (q to quit): ')
#     if food.lower() == 'q':
#         break
#     elif menu.get(food) is not None:
#         card.append(food)
#
# for food in card:
#     total  += menu.get(food)
#
# print(total)




