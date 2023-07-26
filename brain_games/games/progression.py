import random

MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 5

MIN_NUMBER = 1
MAX_NUMBER = 50

MIN_ITEM_LENGTH = 6
MAX_ITEM_LENGTH = 10


def generate_question():
    item = []
    step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    for x in range(random.randint(MIN_ITEM_LENGTH, MAX_ITEM_LENGTH)):
        num += step
        item.append(num)
        item.sort()
    correct_answer = item[random.randint(0, x)]
    for value, index in enumerate(item):
        if index == correct_answer:
            item[value] = '..'
    return (f"{' '.join(str(i) for i in item)}"), str(correct_answer)
