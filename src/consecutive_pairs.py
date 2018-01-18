"""Simple Consecutive Pairs, CodeWars Kata, level 7."""


def consec_pairs(alist):
    """Return count of consecutive pairs in list, last one does not count.

    input = ints, positive and negative, in a list
    output = int, count of consecutive pairs (i.e. one absolute no separation)
    ex: ([1,2,5,8,-4,-3,7,6,5]) = 3
    i.e. [(1,2),(5,8),(-4,-3),(7,6),5] 1, 2 consecutive therefore count = 1
        and so on
    """
    count = 0
    blist = alist[::]
    len_l = len(alist)
    if len_l % 2 == 1:
        blist = alist[:-1]
    blist = zip(alist[0::2], alist[1::2])
    for el in blist:
        if abs(el[0] - el[1]) == 1:
            count += 1
    return count


def pairs(ar):
    """Solution by the_Hamster in CodeWars best practices."""
    count = 0
    for i in range(0, len(ar), 2):
        try:
            a, b = ar[i], ar[i + 1]
        except IndexError:
                return count
        if abs(a - b) == 1:
            count += 1
    return count
