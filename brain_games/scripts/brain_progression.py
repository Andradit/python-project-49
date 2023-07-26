#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import progression


def main():
    engine.run_game(progression.generate_question, 'What number is missing '
                    'in the progression?')


if __name__ == '__main__':
    main()
