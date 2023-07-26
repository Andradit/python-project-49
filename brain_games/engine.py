import prompt


def run_game(question, description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{description}')
    for n in range(0, 3):
        question_and_answer = question()
        print(f'Question: {question_and_answer[0]}')
        answer = prompt.string('Your answer: ')
        if answer == question_and_answer[1]:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{question_and_answer[1]}'. "
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
