"""Hero's Root, CodeWars Kata, level 7."""

import math


def int_rac(n, guess):
    """Return count of integer approximations the integer makes.

    input: ints, two parameters:
        guess = integer, guess
        n = integer, to find square root
    output: return count of integers in a list
    hero's approx: (guess + n / 2) / 2
    e = error set to 1
    """
    e = 1
    new_guess = 0
    res = [guess]
    potato = True
    while potato:
        new_guess = math.floor((guess + n / guess) / 2)
        if abs(res[-1] - new_guess) < abs(e):
            potato = False
            break
        res.append(new_guess)
        guess = new_guess
    return len(res)
