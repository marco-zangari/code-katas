"""Highest and the Lowest, CodeWars Kata, level 7."""


def high_and_low(s):
    """Return the highest and lowest number in the given string.

    input = string, space separated integers
    output = output highest first + space + lowest number
    ex. high_and_low("1 2 3 4 5") returns "5 1"
    ex. high_and_low("1 2 -3 4 5") returns "5 -3"
    ex. high_and_low("1 9 3 4 -5") returns "9 -5"
    """
    res = []
    sp = s.split(' ')
    for num in sp:
        res.append(int(num))
    high, low = max(res), min(res)
    return str(high) + ' ' + str(low)
