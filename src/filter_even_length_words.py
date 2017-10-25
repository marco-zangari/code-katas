"""
Kata Filter Even Length Words - Use a filter function to select even length words

#1 Best Practices: ph162 et al.
def filter_even_length_words(words):
    return [word for word in words if len(word) % 2 == 0]
."""

def filter_even_length_words(words):
    """Filters list of strings to return even lengthed strings."""
    return list(filter(lambda x: len(x) % 2 == 0, words))