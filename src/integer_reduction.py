"""Integer Reduction, Codewars kata, level 6. As of Jan. 22 incomplete."""


def solve(n, k):
    """Return list smalles number from given integers with k elements removed.

    input: integers(n), integer(k)
    output: list, with k integers removed, and original order retained
    ex: solve(123056,4) = '05'
    ex: solve(1284569,2) = '12456'
    """
    n_st = list(str(n)[::])
    o_st = list()
    while len(str(n)) - len(n_st) < k:
        if len(n_st) == 3:
            rem = max(n_st)
            n_st.remove(rem)
            return ''.join(n_st)
        for idx, ch in enumerate(n_st[:-1]):
            if n_st[idx] > n_st[idx + 1]:
                pass
            else:
                o_st.append(ch)
        n_st = o_st + list(n_st[-1])
        o_st = list()
    return ''.join(n_st)


def solve_1(n, k):
    """."""
    n_st = list(str(n)[::])
    if '0' not in n_st:
        for i in range(k):
            rem = max(n_st)
            n_st.remove(rem)
        return n_st
    else:
        x = n_st.index('0')
        left = n_st[:x]
        right = n_st[x + 1:]
        if len(left) >= k:
            for i in range(k):
                rem = max(left)
                left.remove(rem)
            output = ''.join(left + list(n_st[x]) + right)
            return output
        else:
            y = len(left)
            del left
            z = k - y
            for i in range(z):
                rem = max(right)
                right.remove(rem)
            output = ''.join(list(n_st[x]) + right)
            return output
