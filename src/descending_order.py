"""Descending Order, Codewars Kata."""


def descending_order(num):
    """Return non-negative integer input into descending order.

    i.e. return the highest number possible from the given numbers
    input = integer
    output = integer sorted in descending order
    ex. Input: 21445 Output: 54421
    ex. Input: 145263 Output: 654321
    ex. Input: 1254859723 Output: 9875543221
    """
    new_num = sorted(str(num))
    the_join = (''.join(new_num))[::-1]
    return int(the_join)
