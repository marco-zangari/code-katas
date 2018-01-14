"""CodeWars Consecutive Strings."""


def consec_strings(strarr, k):
    """Return k number consecutive strings in string / integer list.

    input = an array string, ex. (["zone", "abigail", "theta",]2)
    k = int, num of strings to go forward
    n = length of string array, ex. 4 = (["zone", "abigail", "theta",]2)

    output = return k number of strings starting with longest in list
        ex. "abigailtheta" from (["zone", "abigail", "theta",]2)

    """
    n = len(strarr)
    res = ""
    concat = ""
    if n == 0 or k > n or k <= 0:
        return ""
    for el in cut_st:
        if len(el) > len(res):
            res = el
    for idx, el in enumerate(strarr):
        if el == res:
            concat = strarr[idx:idx + k]
            break
    return ''.join(concat)


def con_str(strarr, k):
    """."""
    n = len(strarr)
    res = ""
    if n == 0 or k > n or k <= 0:
        return ""
    for el in strarr:
        if len(el) > len(res):
            res = el
    for idx, el in enumerate(strarr):
        if el == res:
            if len(strarr[idx:idx + k]) > len(strarr[:k - idx]):
                return ''.join(strarr[idx: idx + k])
            else:
                return ''.join(strarr[:idx - k])
