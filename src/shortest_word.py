"""Shortest Word, CodeWars Kata, level 7."""


def shortest_word(s):
    """Return length of shortest word in string.

    input = list of strings
    output = integer, length of shortest word
    """
    sp_s = s.split(' ')
    holder = [sp_s[0]]
    for word in sp_s:
        if len(word) < len(holder[0]):
            holder.pop()
            holder.append(word)
    return len(holder[0])
