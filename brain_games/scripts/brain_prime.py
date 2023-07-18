#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for n in range(0, 3):
        num = random.randint(0, 50)
        print(f"Question: {num}")
        print("Your answer: ")
        answer = input()
        correct_answer = ""
        for i in range(2, num):
            if num % i != 0:
                correct_answer = "yes"
            else:
                correct_answer = "no"
                break
        if num == 2:
            correct_answer = "yes"
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
