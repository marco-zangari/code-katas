"""Count the Digit, CodeWars Kata, level 7.

Kata asks for different output than what is given here.
"""


def nb_dig(n, d):
    """Return number of times digit occurs in squares of number.

    input: integers, parameter n represents a number greater than 0
                    parameter d is the digit to look for

    output: integer, count of digits in d
    ex: 10, 1 k*k = 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
            1 in 1, 16, 81, 100 QED count = 4
    """
    count = 0
    res = []
    for num in range(n):
        k = num * num
        for kay in str(k):
            if kay == str(d):
                res.append(str(kay))
    num_str = ''.join(res)
    for digit in num_str:
        if digit == str(d):
            count += 1
    return count


def digit(n, d):
    """."""
    count = 0
    res = []
    for num in range(n + 1):
        k = num * num
        for kay in str(k):
            if kay == str(d):
                res.append(str(kay))
                count += 1
    return count
