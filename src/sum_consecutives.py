"""CodeWars Challenge: Sum Consecutives."""


def sum_consecutives(s):
    """Sum integers together that are same and consecutive.

    input: list with integers (pos, neg, or both)
    output: one list
    ex: [1,4,4,4,0,4,3,3,1] returns [1,12,0,4,6,1]
    ex: [-5,-5,7,7,12,0] returns [-10,14,12,0]
    """
    st = str(s)
    res = []
    total = 0
    for i, num in enumerate(st):
        if num[i] == num[i + 1]:
            total += int(num[i] + num[i + 1])
            res.append(total)
            total = 0
        else:
            res.append(num)
    return res
