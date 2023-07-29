import random
import math

MIN_NUMBER = 1
MAX_NUMBER = 30
DESCRIPTION = ('Find the greatest common '
               'divisor of given numbers.')


def generate_question():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = math.gcd(num_1, num_2)
    return f'{num_1} {num_2}', str(correct_answer)
