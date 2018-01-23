"""Who likes it, Codewars Kata, level 6."""


def likes(ar):
    """Return a string of who likes the post.

    input = string with name(s)
    output = string with name + like(s) this
    ex: likes [] // must be "no one likes this"
        likes ["Peter"] // must be "Peter likes this"
        likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
        likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
        likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
    """
    len_ar = len(ar)
    if len_ar == 0:
        return "no one likes this"
    if len_ar == 1:
        return "%s likes this" % (ar[0])
    if len_ar == 2:
        return "%s and %s like this" % (ar[0], ar[1])
    if len_ar == 3:
        return "%s, %s and %s like this" % (ar[0], ar[1], ar[2])
    if len_ar > 3:
        return "%s, %s and %d others like this" % (ar[0], ar[1], (len_ar - 2))
