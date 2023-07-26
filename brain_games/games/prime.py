import random

MIN_NUMBER = 1
MAX_NUMBER = 50


def generate_question():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = ''
    for i in range(2, num):
        if num % i != 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
            break
    if num == 2:
        correct_answer = 'yes'
    return num, correct_answer
