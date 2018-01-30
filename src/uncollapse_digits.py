"""Uncollapse Digits, codewars kata, level 6. unfinished as of jan. 23, 2018."""


def uncollapse(s):
    """Return uncollapse digit string.

    input: string
    output: string with spaces between numbers
    ex: fivethreefivesixthreenineonesevenoneeight -> five three five six three nine one seven one eight
    """
    res = ''
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine']
    for num in numbers:
        for idx, num in enumerate(len(s) - 1):
            res = ' ' + num[idx] + ' '
    return res
