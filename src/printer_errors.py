"""Printer Errors, CodeWars Kata, level 7."""


def printer_error(s):
    """Return error rate of printer.

    Input = string
    Output = string, with numerator as error, denominator as instances
    """
    denom = str(len(s))
    count = 0
    lettr_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for letter in s:
        if letter not in lettr_l:
            count += 1
    return str(count) + '/' + denom
