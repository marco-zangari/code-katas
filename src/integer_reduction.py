"""Integer Reduction, Codewars kata, level 6."""


def solve(n, k):
    """Return list smalles number from given integers with k elements removed.

    input: integers(n), integer(k)
    output: list, with k integers removed, and original order retained
    ex: solve(123056,4) = '05'
    ex: solve(1284569,2) = '12456'
    """
    n_st = list(str(n)[::])
    if not '0' in n_st:
        for i in range(k):
            rem = max(n_st)
            n_st.remove(rem)
        return n_st
    else:
        x = n_st.index('0')
