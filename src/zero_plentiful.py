"""Zero Plentiful Code Kata, codewars."""

def zero_plentiful(arr):
    """."""
    four_zero_plus = 0
    count = 0
    if arr == [0]:
        return 0
    if len(arr) == arr.count(0):
        return 1
    for idx, el in enumerate(arr):
        if el == 0:
            count += 1
        if el != 0 or idx == len(n) - 1:
            if count >= 4:
                four_zero_plus += 1
            if count > 0 or count < 4:
                return 0
    return four_zero_plus

def zero_plentiful2(arr):
    """Zero plentiful list is at least one zero and four zeros in sequence.

    input= list of integers
    output= either number of times of four zero sequences
            or 0 (for no four sequences)
    """
    four_zero = 0
    count = 0

    for el in arr:
        if el == 0:
            count += 1
            if count >= 4:
                four_zero += 1
                count = 0
            if el != 0 and count < 4:
                return 0
        if el != 0 and count > 0:
            return 0
        if el != 0:
            count = 0
    if four_zero > 0:
        return four_zero
    else:
        return 0


def zero_plentiful3(arr):
    """."""
    four_plus = 0
    res = []
    for char in arr:
        if char == 0:
            res.append(char)
        if char != 0:
            if len(res) >= 4:
                four_plus += 1
                for x in res:
                    res.pop()
            if len(res) < 4 and len(res) > 0:
                return 0
    return four_plus


def str_maker(arr):
    """Make a string from list of integers."""
    res = []
    for num in arr:
        res.append(str(num))
    output = ''.join(res)
    return output


def zero_plentiful4(arr):
    """."""
    four_zero = 0
    count = 0
    if arr == [0]:
        return 0
    elif len(arr) == arr.count(0):
        return 1
    else:
        for el in arr:
            if el == 0:
                count += 1
                if count >= 4:
                    four_zero += 1
                    count = 0
                if el != 0 and count < 4:
                    four_zero = 0
                    return 0
            if el != 0 and count > 0:
                four_zero = 0
                return 0
            if el != 0:
                count = 0
        if four_zero > 0:
            return four_zero
        else:
            return 0