"""Code Kata: Grouped by Commas in CodeWars, level 6."""


def commas(num):
    """Add commas after every three-number group to create decimal represenation.

    input = integer
    output = string with comma separations
    ex. input = 10, output = 10
    ex. input = 1000, output = 1,000
    """
    str_num = str(num)
    res = [str_num[0]]
    for idx in range(1, len(str_num)):
        if (len(str_num) - idx) % 3 == 0:
            res.append(',')
        res.append(str_num[idx])
    return ''.join(res)
