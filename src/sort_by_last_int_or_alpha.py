"""Sort Array by Last Character, Codewars Kata, level 7. Unfinished as of Jan. 19."""


def sort_last1(li):
    int_holder = []
    char_holder = []
    for el in li:
        if type(el) == int:
            int_holder.append(el)
        if type(el) == str:
            char_holder.append(el)
    for char in char_holder:



    rev_int = sorted(int_holder)
    rev_char = sorted(char_holder)


def sort_last(li):
    """Sort the last character in list either an integer or alpha char.

    input = character or integer in a string list
    output = the last character or integer in the list
    ex: sortMe(['acvd','bcc']) => ['bcc','acvd']
    """
    copy = li[::]
    res = []
    output = []
    final = []
    for el in copy:
            rev = str(el)[::-1]
            res.append(rev)
    for x in sorted(res):
        un_rev = x[::-1]
        output.append(un_rev)
    for el in output:
        if str(el) not in li:
            final.append(int(el))
            continue
        final.append(el)
    return final