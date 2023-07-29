import random

MIN_NUMBER = 0
MAX_NUMBER = 10
DESCRIPTION = ('What is the result of the '
               'expression?')


def generate_question():
    operations = ['+', '-', '*']
    operand = random.choice(operations)
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num_1} {operand} {num_2}'
    if operand == '+':
        correct_answer = num_1 + num_2
    elif operand == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
