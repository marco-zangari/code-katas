"""Find missing numbers, CodeWars Kata, level 7."""


def find_nums(a):
    """Find the missing numbers in a given list.

    input = integers, consecutive, positivea and negative with gaps
    output = integers, that fill in gaps of input
    """
    res = []
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) != 1:
            res.append(a[i] + 1)
    return res
