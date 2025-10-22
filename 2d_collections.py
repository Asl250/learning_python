# vegetables = ['carrot', 'tomato', 'cucumber']
# fruit = ['apple', 'orange', 'banana']
# meat = ['chicken', 'fish', 'turkey']
#
# groceries = [vegetables, fruit, meat]
#
# for i in groceries :
#     for food in i :
#         print(food, end=' ')


# num_pad = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     ('*', 0, '#'))
#
# for i in num_pad:
#     for num in i:
#         print(num, end=' ')
#     print()


# QUIZ

questions = (
    'how many elements on the periodic table: ',
    'which animal lays the biggest eggs: ',
    'how many bones in the human: ',
    'which planet in the solar system is the hottest: '
)

options = (
    ('A.116,', 'B.117', 'C.118'),
    ('A.Whale', 'B.elephant', 'C.ostrich'),
    ('A.206', 'B.207', 'C.208'),
    ('A.Mercury', 'B.Venus', 'C.Mars')
)

answers = ('C', 'C', 'A', 'B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('--------------')
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input('enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('correct!')
    else:
        print('incorrect!')
        print(f'correct answer was {answers[question_num]}')
    question_num += 1

print('---------------')
print(f'Your score is the {score} correct answers')
print('---------------')


