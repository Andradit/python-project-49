#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    for n in range(0, 3):
        ops = ['+', '-', '*']
        operation = random.choice(ops)
        num_1, num_2 = random.randint(0, 100), random.randint(0, 100)
        print(f"Question: {num_1} {operation} {num_2}")
        print("Your answer: ")
        answer = int(input())
        correct_answer = eval(f'{num_1} {operation} {num_2}')
        # try:
        #     answer = int(answer)
        # except ValueError:
        #     print(f"Please enter your answer in numbers. "
        #           f"Let's try again, {name}!")
        #     return
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
