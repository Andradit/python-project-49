#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import calc


def main():
    engine.run_game(calc.generate_question, 'What is the result of the '
                    'expression?')


if __name__ == '__main__':
    main()
