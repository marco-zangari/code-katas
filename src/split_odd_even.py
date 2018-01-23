"""T.T.T.17: Split Odd and Even, Codewars Kata, level 6."""


def split_odd_even(ar):
    """Return a list that contains continuous parts of odd and even nums.

    input: list of integers
    output: a list with integers separated into continuous even and odd digits
    ex: split(123)  ===  [1,2,3]
        split(223)  ===  [22,3]
        split(111)  ===  [111]
        split(13579)  ===  [13579]
        split(135246)  ===  [135,246]
        split(123456)  ===  [1,2,3,4,5,6]
    """
    if not ar:
        return -1
    st_a = str_num(ar)
    res = [st_a[0]]
    for ch in st_a[1:]:
        if int(ch) % 2 == 0:
            if int(res[-1]) % 2 == 0:
                res[-1] += ch
            else:
                res.append(ch)
        else:
            if int(res[-1]) % 2 == 1:
                res[-1] += ch
            else:
                res.append(ch)
    return res


def str_num(n):
    """."""
    res = []
    for num in str(n):
        res.append(num)
    return res
