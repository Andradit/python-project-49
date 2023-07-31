import random
# import math

MIN_NUMBER = 1
MAX_NUMBER = 50
DESCRIPTION = ('Answer "yes" if given '
               'number is prime. Otherwise answer "no".')


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        elif num == 0 or num == 1:
            return False
    return True


def generate_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = ''

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer
