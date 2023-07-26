import random

MIN_NUMBER = 1
MAX_NUMBER = 30


def generate_question():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    for divisor in range(1, 31):
        if (num_1 % divisor) == 0 and (num_2 % divisor) == 0:
            correct_answer = divisor
    return f'{num_1} {num_2}', str(correct_answer)
