import random

MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 5

MIN_NUMBER = 1
MAX_NUMBER = 50

MIN_ITEM_LENGTH = 6
MAX_ITEM_LENGTH = 10

DESCRIPTION = ('What number is missing '
               'in the progression?')


def generate_progression(length, start, step):
    item = []
    for x in range(length):
        start += step
        item.append(start)
    return item


def generate_question():
    length = random.randint(MIN_ITEM_LENGTH, MAX_ITEM_LENGTH)
    step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = generate_progression(length, start, step)
    correct_answer_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_index]
    progression[correct_answer_index] = '..'
    return ' '.join(str(i) for i in progression), str(correct_answer)
