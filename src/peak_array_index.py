"""Peak Array Index, CodeWars Kata, level 7."""


def peak_index(li):
    """Return index of integer when left integer sum equals right integer sum.

    input = integers, list
    output = integer, the index of the value
    edge = if not possible for peak, return -1
    ex. [1,2,3,5,3,2,1] = 3 because left = [1 + 2 + 3] right = [3 + 2 + 1]
    ex. [1,12,3,3,6,3,1] = 2
    ex. [10,20,30,40] = -1
    """
    if not li:
        return -1
    if len(li) < 3:
        return -1
    l_sum = li[0]
    r_sum = li[-1]
    i = 1
    j = (len(li) - 1) - 1
    while i < (len(li) - 1):
        for idx in range(1, len(li) - 1):
            if l_sum == r_sum:
                if abs(i - j) == 2:
                    if i < j:
                        return i + 1
                    else:
                        return j - 1
                elif i == j:
                    return i
                else:
                    l_sum += li[i]
                    r_sum += li[j]
                    i += 1
                    j -= 1
            else:
                if l_sum < r_sum:
                    l_sum += li[i]
                    i += 1
                else:
                    r_sum += li[j]
                    j -= 1
    return -1
