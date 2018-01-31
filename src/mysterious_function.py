"""Mysterious Function, codewars kata, level 6."""


def mysterious_func(nums):
    """Find the holes.

    input: int, number
    output: int, count of how many holes
    ex: getNum(300) #-> returns 2
        getNum(90783) #-> returns 4
        getNum(123321) #-> returns 0
        getNum(89282350306) #-> returns 8
        getNum(3479283469) #-> returns 5
    """
    holes = [0, 6, 8, 9]
    hole_count = 0
    num_st = str(nums)
    for num in num_st:
        if num in holes:
            hole_count += 1
    return hole_count
