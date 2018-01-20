"""Without the letter 'E', CodeWars Kata, level 7."""


def with_without_e(s):
    """Return number of Es in string.

    input = string
    output = count in string form of Es
    """
    if not s:
        return s
    count = 0
    for e in s:
        if e == 'e' or e == 'E':
            count += 1
    if count == 0:
        return 'There is no "e".'
    else:
        st_count = str(count)
        return st_count
