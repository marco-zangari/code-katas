"""Sort by Last Char, Codewars Kata, level 7."""


def last(s):
    """Return a word string sorted alpha-ly by last char in each word.

    input = string, words
    output = string, sorted words alphabetically by last char
    ex: "man i need a taxi up to ubud") ==>["a", "need", "ubud", "i", "taxi", "man", "to", "up"]

    """
    alpha = list(map(chr, range(97, 123)))
    output = []
    sp_s = s.split()

    for ch in alpha:
        for word in sp_s:
            if ch == word[-1]:
                output.append(word)
    return output
