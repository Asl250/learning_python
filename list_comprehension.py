# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
#
# print(doubles)

# doubles = [i*2 for i in range(1,11)]
# triples = [i*3 for i in range(1,11)]
# squares = [i*i for i in range(1,11)]
#
# print(squares)

# fruits = ['apple', 'coconut', 'pineapple', 'banana', 'watermelon']
# fruit_chars = [i[0] for i in fruits]
# print(fruit_chars)



# numbers = [1, -2, 3, -4, 5, -6]
# positive_numbers = [i for i in numbers if i >= 0]
# negative_numbers = [i for i in numbers if i < 0]
# even_num = [i for i in numbers if i%2 == 0]
# odd_num = [i for i in numbers if i%2 == 1]
#
# print(odd_num)


grades = [85, 43,  67, 90, 13]
passing_grades = [i for i in grades if i >= 65]
print(passing_grades)