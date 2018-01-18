"""Greatest Difference, CodeWars Kata, level 7."""


def greatest_diff(a):
    """Find the greatest difference between string couples.

    input = list of strings of numbers in pairs
    output = string, with the pair that has greatest difference
    ex: ['1-3','5-7','2-3'] should be '1-3' because greatest difference
        and before '5-7'
    """
    diff_count = 0
    difference = []
    res = []
    for coup in a:
        coup_spl = coup.split('-')
        diff = abs(int(coup_spl[0]) - int(coup_spl[1]))
        difference.append(diff)
        if diff > diff_count:
            diff_count = diff
            res.append(coup)
    if diff_count == 0:
        return False
    else:
        return res.pop()


def diff1(arr):
    """kevin.du on CodeWars solutions."""
    b = 0
    c = 0
    for i in arr:
        a = eval(i)
        if abs(a) > c:
            b = i
            c = abs(a)
    return b


def diff2(arr):
    """Luisho5 on CodeWars solutions."""
    r = 0
    c = ''
    for i in arr:
        y = i.split('-')
        s = abs(int(y[0]) - int(y[1]))
        if s > r:
            r = s
            c = i
    if r == 0: return False
    return c
