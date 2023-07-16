#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    for n in range(0, 3):
        num_1, num_2 = random.randint(1, 30), random.randint(1, 30)
        print(f"Question: {num_1} {num_2}")
        print("Your answer: ")
        answer = int(input())
        for divr in range(1, 31):
            if (num_1 % divr) == 0 and (num_2 % divr) == 0:
                correct_answer = divr
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}. "
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
