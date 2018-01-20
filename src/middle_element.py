"""Find the Middle Element, Codewars Kata, level 7."""


def find_middle_el(li):
    """Return the index of the element that numberical lies in middle.

    input = list of three numbers
    output = index of number whose value lies between other two
    ex: [2, 3, 1] => 0
    ex: [5, 10, 14] => 1
    """
    high, low = max(li), min(li)
    for x in li:
        if x != low and x != high:
            return li.index(x)
