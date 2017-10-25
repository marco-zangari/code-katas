"""
Kata: Simple Pig Latin - Return each word with first letter removed and added to end of word with the addition of 'ay'

#1 Best Practices Solution by dykchui et al.

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
."""


def pig_it(text):
    """Removes first letter of an original word and returns a new word with original word's first letter at end with addition of 'ay'."""
    pyg = 'ay'
    text_var = text.split()
    each_word = []
    for item in text_var:
        if len(item) > 0 and item.isalpha():
          each_word.append(item[1:] + item[0] + pyg)
        else:
          each_word.append(item)
    return ' '.join(each_word)