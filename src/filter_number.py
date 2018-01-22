"""Filter the Number, Codewars Kata, level 7."""


def filter_num(a):
    """Return only numbers from a mixed string of chars and nums."""
    res = []
    for el in a:
        if el.isdigit():
            res.append(el)
    output = int(''.join(res))
    return output
