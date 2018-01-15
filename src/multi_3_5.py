"""Code Kata Multiples of 3 or 5."""


def multi_3_5(nums):
    """Find multiples of three or five return sum of non-repeating nums.

    Given a number, find its multiples of three or five
    input = natural number
    output = sum non-repeating natural numbers
    ex input = 10, ex output = 23, i.e. [3, 5, 6, 9]
    ex input = 20, ex output = 78, i.e. [3, 5, 6, 9, 10, 12, 15, x15x, 18]
    """
    threes = []
    fives = []
    for num in range(nums):
        if num % 3 == 0:
            threes.append(num)
        if num % 5 == 0:
            fives.append(num)
    cumulnum = sum(set(threes + fives))
    return cumulnum
