"""Kata in codewrs. Called: Stop gninnipS My sdroW!.

A Code challenge to reverse words in a string
"""


def spin_words(sentence):
    """Spin words greater than five char long in a string.

    preserving white spaces
    """
    temp = []
    spl = sentence.split()
    for char in spl:
        if len(char) >= 5:
            spin = char[::-1]
            temp.append(spin)
        else:
            temp.append(char)
    output = ' '.join(temp)
    return output
