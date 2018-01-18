"""Find missing numbers, CodeWars Kata, level 7."""


def find_nums(a):
    """Find the missing numbers in a given list.

    input = integers, consecutive, positivea and negative with gaps
    output = integers, that fill in gaps of input
    """
    res = []
    comp = list(range(a[0], a[-1]))
    for num in a:
        if num not in comp:
            res.append(num)
    return res
