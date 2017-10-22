"""Kata: Move All Vowels - Remove all vowels from a word and place at end of word in order of removal.

#1 Best Practices Solution daddepledge

def move_vowels(s):
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))
."""

def move_vowels(x):
	"""Removes vowels from single word. Places them at end of new word."""
    vowel_str = 'aeiou'
    con_string = ''
    vowel_string = ''

    for item in x:
        if vowel_str.find(item) >= 0:
            vowel_string = vowel_string + item
        else:
            con_string = con_string + item
    return con_string + vowel_string