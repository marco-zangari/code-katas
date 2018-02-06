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

if __name__ == '__main__':
    s = 'abccdefee'
    remove_unique(s)
