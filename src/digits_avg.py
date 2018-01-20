"""Digits Average, CodeWars Kata, level 7."""


def digitsaverage(d):
    """Return the average of the digits until number is one digit.

    input = integer
    output = integer, single digit
    ex. 246 = 4 i.e. avg of 2 and 4 is 3, average of 4 and 6 is 5
        so after first iteration 246 => 35
        avg of 3 and 5 is 4 so digitsAverage(246) returns 4
    """
    if not d:
        return d
    res = ''
    if d < 10:
        return d
    else:
        st_d = str(d)
        for x in range(len(st_d) - 1):
            z = st_d[x]
            y = st_d[x + 1]
            float = (int(z) + int(y)) % len(z + y)
            avg = ((int(z) + int(y)) // len(z + y)) + float
            res += str(avg)
        recurs = int(res)
        return digitsaverage(recurs)
