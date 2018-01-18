"""CodeWars Kata Called Simple string."""


def simp_str(str):
    """Return a integer list to count: upper-, lowercase, numbers, and spec. ch.

    input = string
    output = list of integers, to count
    ex: if input is "*'&ABCDabcde12345"), output: [4,5,5,3].
    the order is: uppercase letters, lowercase, numbers and special characters.
    """
    len_str = len(str)
    upper = 0
    lower = 0
    nums = 0
    spec = 0
    for el in str:
        if el.isupper():
            upper += 1
        if el.islower():
            lower += 1
        if el.isdigit():
            nums += 1
    spec = len_str - (upper + lower + nums)
    return [upper, lower, nums, spec]
