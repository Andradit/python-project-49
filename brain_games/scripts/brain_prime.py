#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import prime


def main():
    engine.run_game(prime.generate_question, "Answer 'yes' if given "
                    "number is prime. Otherwise answer 'no'.")


if __name__ == '__main__':
    main()
