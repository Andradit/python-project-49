#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    for n in range(0, 3):
        item = []
        step = random.randint(1, 5)
        num = random.randint(1, 50)
        for x in range(random.randint(6, 10)):
            num += step
            item.append(num)
            item.sort()
        correct_answer = item[random.randint(0, x)]
        for i, var in enumerate(item):
            if var == correct_answer:
                item[i] = '..'
        print(f"Question: {' '.join(str(i) for i in item)}")
        print("Your answer: ")
        answer = int(input())
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
