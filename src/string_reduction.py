"""String Reduction, Codewars Kata, level 6."""

import collections


def string_reduction(ar1, ar2):
    """Return number of characters to be eliminated from ar1 to get ar2.

    input = two strings, characters
    output = integer, difference between ar1 and eliminated ar1
    ex: solve("aabcdefg","fbd") = 5
    ex: solve("xyz","yxxz") = 0
    """
    if len(ar1) < len(ar2):
        return 0
    count_1 = 0
    count_2 = 0
    dict_ar1, dict_ar2 = histogram(ar1), histogram(ar2)
    vals_1, vals_2 = dict_ar1.values(), dict_ar2.values()
    for val in vals_2:
        count_2 += val
    for val in vals_1:
        count_1 += val
    return count_1 - count_2


def histogram(ar):
    """Return key and value from string."""
    d = dict()
    for c in ar:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
