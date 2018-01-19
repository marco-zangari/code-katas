"""Two to One, CodeWars Kata, level 7."""


def longest(s1, s2):
    """Return longest sorted string of distinct letters from two strings.

    input = 2 strings, characters are a-z
    output = 1 string, with distinct characters from both
    ex: a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
    """
    concat = s1 + s2
    set_up = set(concat)
    s_set_up = sorted(set_up)
    output = ''.join(s_set_up)
    return output
