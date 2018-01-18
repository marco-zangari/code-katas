"""Minimize_sum_Of_array!!!, CodeWars Kata, level 7."""


def minimize_sum(arr):
    """Minimize sum of array.

    Find pairs of to multiply then add the product of those multiples
    to find the minimum possible sum

    input = integers, in a list
    output = integer, the minimum sum of those products
    ex: minSum(5,4,2,3) should return 22, 5*2 +3*4 = 22
    ex: minSum(12,6,10,26,3,24) should return 342, 26*3 + 24*6 + 12*10 = 342
    """
    x = len(arr)
    res = []
    arr1 = sorted(arr)
    for i in range(x // 2):
        minprod = arr1[0] * arr1[-1]
        arr1.pop()
        arr1.pop(0)
        res.append(minprod)
    return sum(res)
