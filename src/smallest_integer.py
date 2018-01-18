"""Find the smallest integer in the array, Kata in Codewars."""


def smallest(alist):
    """Return the smallest integer in the list.

    input: a list of integers
    output: a single integer
    ex: [34, 15, 88, 2] should return 34
    ex: [34, -345, -1, 100] should return -345
    """
    res = [alist[0]]
    for num in alist:
        if res[0] > num:
            res.pop()
            res.append(num)
    return res[0]
