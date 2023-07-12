#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    # print("May I have your name?")
    # name = input()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for n in range(0, 3):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        print("Your answer: ")
        answer = input()
        correct_answer = ""
        if number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
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
