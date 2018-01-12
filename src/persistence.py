"""Kata in codewars: Persistent Bugger."""


def persistence(n):
    """Take in positive parameter; return multiplicative persistence.

    input: integer
    output: integer, number of times input persists until reaches single digit.
    ex: persistence(39) = 3, (1) 3 * 9 = 27, (2) 2 * 7 = 14, (3) 1 * 4 = 4
    """
    count = 0
    if n < 10:
        return count
    else:
        count += 1
        quot, rem = divmod(n, 10)
        persistence(quot * rem)
    return count
