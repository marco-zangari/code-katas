"""Code Kata from codewars called simple fun #78: Build Palindrome.

input = a string
output = a string

a string conisting of lowercase letters
constraints: 3 <= str length <= 10
"""


def is_palin(word):
    """."""
    if word[::-1] == word:
        return True
    else:
        return False


def palin_build(s):
    """Build palindrome from string letter sequence."""
    for i in range(len(s)):
            if is_palin(s[i:]):
                return s + s[:i][::-1]


def short_palin(s):
    """."""
    init_suff = s[-2] + s[-1]
    i = len(s) - 1 - len(init_suff)
    suffix = init_suff
    check = s[i:]

    while i > 0:
        new_suff = s[i] + suffix
        if is_palin(new_suff) is True:
            suffix = check
            i -= 1

        else:
            break

    if is_palin(s[:i + 1]) == True:
        palin = s[:i + 1] + suffix + s[0]
        return palin
    else:
        palin = s[:i + 1] + suffix + s[:i + 1][::-1]
        return palin
