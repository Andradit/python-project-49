import random

MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = ('Answer "yes" if the '
               'number is even, otherwise answer "no".')


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def generate_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = ''

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(number), correct_answer
