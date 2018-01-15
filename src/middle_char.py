"""Get the Middle Character Code Wars Kata."""


def get_mid(str):
    r"""Return middle character(s) of string input.

    input = string
    output = string
    ex input, 'test\0' should return 'es'
    ex input, 'tests\0' should return 's'
    """
    st = str[:-1]
    len_st = len(st)
    if len_st % 2 == 1:
        a = len_st // 2
        return st[a]
    if len(st) % 2 == 0:
        a = len_st // 2
        return st[a - 1:a + 1]
