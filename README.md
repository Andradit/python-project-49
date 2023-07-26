### Hexlet tests and linter status:
[![Actions Status](https://github.com/Andradit/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Andradit/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1cc7b38eb837cfaaa97e/maintainability)](https://codeclimate.com/github/Andradit/python-project-49/maintainability)

Five single-choice math games!

## Instructions

You are offered a choice of 5 math games, in each of which, you need to give the correct text or numerical answer depending on the proposed task.

Before starting the game, you will need to write your name.

List of games offered:

***Brain Even*** - you are shown a random number. You must answer "yes" if the number is even or "no" if it is odd.

***Brain Calc*** - you are shown an arbitrary mathematical expression, such as "35 + 16", which you must calculate and write down the correct answer.

***Brain GCD*** - you are shown two random numbers, e.g. "25 50". You must calculate and enter the greatest common divisor of these numbers.

***Brain Progression*** - you are shown a series of numbers forming an arithmetic progression in which any of the digits is replaced by two dots. You must identify this number.

***Brain Prime*** - you're shown a random number. You have to answer "yes" if the number is prime or no if it is not:

### Installation

> ```diff
> + Please report issues if you try to install and run into problems!
> ```

Make sure you are running at least Python 3.11

Clone the repository and install manually:

```bash
$ git clone git@github.com:Andradit/python-project-49.git
$ cd python-project-49/
$ make install
$ make build
$ make package-install
```
### Start Brain Even
To start the game, run either:
```bash
$ brain-even
```
You have to answer "yes" or "no".

<script async id="asciicast-MJce7KxZGXgjqL1qikuJ4H65X" src="https://asciinema.org/a/MJce7KxZGXgjqL1qikuJ4H65X.js"></script>

### Start Brain Calc
To start the game, run either:
```bash
$ brain-calc
```
You must calculate and write the correct answer.

[![asciicast](https://asciinema.org/a/GIMMJU9vzL2Muf60665dI6Wne.svg)](https://asciinema.org/a/GIMMJU9vzL2Muf60665dI6Wne)

### Start Brain GCD
To start the game, run either:
```bash
$ brain-gcd
```
You must calculate and enter the greatest common divisor.

[![asciicast](https://asciinema.org/a/02jhA24vr6ozCAE5ujbp582NU.svg)](https://asciinema.org/a/02jhA24vr6ozCAE5ujbp582NU)

### Start Brain Progression
To start the game, run either:
```bash
$ brain-progression
```
You must write the number behind the two dots.

[![asciicast](https://asciinema.org/a/UTPLPKzAxSpsSANVs0nuJGiPS.svg)](https://asciinema.org/a/UTPLPKzAxSpsSANVs0nuJGiPS)

### Start Brain Prime
To start the game, run either:
```bash
$ brain-prime
```
You have to answer "yes" or "no".

[![asciicast](https://asciinema.org/a/ZTuvvX9cfIZgLJ7h3dGIQUdDR.svg)](https://asciinema.org/a/ZTuvvX9cfIZgLJ7h3dGIQUdDR)

#### Possible Improvements

- Color support.
- Increasing the range of numbers offered
- Сreating more complex expressions
- Multiplayer
- *Your* creative idea.

If you encounter any problem or have any suggestions, please [open an issue](https://github.com/Andradit/python-project-49/issues/new) or [send a PR](https://github.com/Andradit/python-project-49/pulls).
