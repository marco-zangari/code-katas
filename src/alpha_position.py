"""Code Challenge Code Wars: Alpha Position."""


def alphabet_position(text):
    """."""
    res = list()
    for ch in text:
        if ch.isalpha():
            num = ord(ch) - 96
            res.append(str(num))
        else:
            pass
    output = " ".join(res)
    return output
