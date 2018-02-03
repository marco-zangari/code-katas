"""Duplicate Encoder, codewars kata, level 6."""


def duplicates(s):
    """Change duplicates to closed parens; all else open parens.

    input = string, of letters
    output = string, of open or closed parens
    ex  "din" => "((("
        "(( @" => "))(("
        "Success" => ")())())"
    """
    lower_s = s.lower()
    res = ''
    x_dict = histogram(lower_s)
    for ch in lower_s:
        if x_dict[ch] > 1:
            res += ')'
        else:
            res += '('
    return res


def histogram(s):
    """."""
    d = dict()
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d
