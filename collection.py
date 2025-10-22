# list[]  set{}  tuple()

# LIST
# fruit = ['apple', 'orange', 'banana']
# dir(fruit)
# print(fruit[::-1])
# print(len(fruit))
#print('apple' in fruit) # is apple exist in list fruit true/false

# fruit[0] = 'pineapple'
# fruit.append('pineapple')
# fruit.remove('apple')
# fruit.insert(0,'pineapple')
#fruit.sort() # sort in alphabetic order
# fruit.reverse()
#fruit.clear() #remove all elements
#fruit.index('apple')

# print(fruit)
# for i in fruit :
#     print(i)



#SET
# animals = {'cat', 'dog', 'elephant', 'crocodile'}
# print(len(animals))
# print('dog' in animals)

# animals.add('tiger') # IT ADDS INTO START OF THE SET
# animals.remove('dog')
# animals.pop()

# print(animals)

# TUPLE
# animals = ('cat', 'dog', 'elephant', 'crocodile')
# print(len(animals))


#shopping card
# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input('enter a food to buy (q to quit): ')
#     if food.lower() == 'q' :
#         break
#     else:
#         price = float(input(f'enter the price of {food}: $'))
#         foods.append(food)
#         prices.append(price)
#
# print('------Your card -------')
#
# for i in foods :
#     print(i, end=' ')
#
# for i in prices:
#     total += i
#
# print()
# print(f'your total is: ${total}', end=' ')