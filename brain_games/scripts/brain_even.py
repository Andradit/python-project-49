#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import even


def main():
    engine.run_game(even.generate_question, "Answer 'yes' if the "
                    "number is even, otherwise answer 'no'.")


if __name__ == '__main__':
    main()
