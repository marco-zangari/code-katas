"""Only Duplicates, codewars code kata, level 6."""


def remove_unique(s):
    """Remove unique elements from a string."""
    res = []
    dict_obj = histo(s)
    for ch in s:
        if dict_obj[ch] == 1:
            pass
        else:
            res.append(ch)
    return ''.join(res)


def histo(s):
    """Create histogram object."""
    d = dict()
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d

if __name__ == '__main__':
    s = 'abccdefee'
    print(f'The string, {s}, yields {remove_unique(s)} as an answer')
