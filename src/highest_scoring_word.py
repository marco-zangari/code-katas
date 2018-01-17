"""Code Challenge Highest Scoring Word, CodeWars, level 6."""


def high_word(strin):
    """Return highest scoring word from a string.

    Input = string, words of lowercase letters
    Output = word in a string with highest value
    ex. values = 'a' = 1, 'b' = 2, ..., 'z' = 26
    ex. input = 'man i need a taxi up to ubud' output = 'taxi'
    """
    a = strin.split()
    outer_list = []
    for word in a:
        word_sum = 0
        inner_list = []
        outer_list.append(inner_list)
        inner_list = []
        for word in a:
            for letter in word:
                word_sum += (ord(letter) - 96)
            inner_list.append(word_sum)
            word_sum = 0
    for idx, x in enumerate(inner_list):
        maxi = max(inner_list)
        if x == maxi:
            return a[idx]
