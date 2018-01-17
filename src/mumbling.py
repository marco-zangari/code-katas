"""Mumbing Kata in Codewars, level 7."""


def accum(astr):
    """Return a each letter of case with n number of same letters.

    input = string, letters either a - z or A - Z
    output = string, one uppercase letter followed by lower case ones,
        and a dash
    ex: 'abcd' should return 'A-Bb-Ccc-Dddd'
    ex: 'RqaEzty' should return 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
    """
    res = []
    for idx, letter in enumerate(astr):
        first_letter = letter.upper()
        res.append(first_letter)
        second_letters = (letter.lower() * idx) + '-'
        res.append(second_letters)
    return ''.join(res)[:-1]
