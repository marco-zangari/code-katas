"""CodeWars Code Kata: Insert dashes.

Insert dashes between two consecutive odd numbers.
"""


def insert_dash(nums):
    """Insert dashes between odd numbers.

    input = numbers
    output = numbers with dashes added
    ex. input 454793 should equal '4547-9-3'
    ex input 1003567 should equal '1003-567'
    """
    str_nums = str(nums)
    res = [str_nums[0]]
    for idx in range(1, len(str_nums)):
        if int(str_nums[idx]) % 2 == 1:
            if int(res[-1]) % 2 == 1:
                res.append('-')
            res.append(str_nums[idx])
        else:
            res.append(str_nums[idx])
    return ''.join(res)


def insert_dash_asterik(nums):
    """Insert asterisk within even numbers and dash within odd ones."""
    str_nums = str(nums)
    res = [str_nums[0]]
    for idx in range(1, len(str_nums)):
        if int(str_nums[idx]) % 2 == 1:
            if int(res[-1]) % 2 == 1:
                res.append('-')
            res.append(str_nums[idx])
        if int(str_nums[idx]) % 2 == 0:
            if int(res[-1]) % 2 == 0 and res[-1] != '0':
                res.append('*')
            res.append(str_nums[idx])
    return ''.join(res)
