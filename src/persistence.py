"""Kata in codewars: Persistent Bugger."""


def persistence(n, count=0):
    """Take in positive parameter; return multiplicative persistence.

    input: integer
    output: integer, number of times input persists until reaches single digit.
    ex: persistence(39) = 3, (1) 3 * 9 = 27, (2) 2 * 7 = 14, (3) 1 * 4 = 4
        persistence(99) = 4, (1) 9 * 9 * 9 = 729, (2) 7 * 2 * 9 = 126, (3) 1 * 2 * 6 = 18, (4) 1 * 8 = 8
    """
    count = 0
    if n < 10:
        return count
    else:
        return persistence(persistence2(n), count + 1)


def persistence2(n):
    """."""
    cumul = 1
    for num in n:
        cumul *= int(num)
    return cumul
