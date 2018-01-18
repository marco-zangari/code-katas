"""Maximum Length Difference, CodeWars Kata, level 7."""


def max_length_diff(a1, a2):
    """Find the maximum length difference between two lists of strings.

    Find max(abs(length(x) − length(y))) where x from s1 and y from s2
    input = two lists, each one has strings of letters a-z
    output = integer difference
    if any list is empty, return -1
    ex:
    s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
                    "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
    s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    mxdiflg(s1, s2) = 13 because 'oox' is (3), and 'cccooommaaqqoxii' is (16)
    """
    if bool(a1) is False or bool(a2) is False:
        return -1
    else:
        minimum1 = a1[0]
        maximum1 = a1[0]
        minimum2 = a2[0]
        maximum2 = a2[0]
        for st in a1:
            if len(st) < len(minimum1):
                minimum1 = st
            if len(st) > len(maximum1):
                maximum1 = st
        for st in a2:
            if len(st) < len(minimum2):
                minimum2 = st
            if len(st) > len(maximum2):
                maximum2 = st
        if abs(len(maximum1) - len(minimum2)) > abs(len(minimum1) - len(maximum2)):
            return abs(len(maximum1) - len(minimum2))
        else:
            return abs(len(minimum1) - len(maximum2))
