import random

MIN_NUMBER = 0
MAX_NUMBER = 100


def generate_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = ''
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(number), correct_answer
