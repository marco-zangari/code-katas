"""Implement a string pyramid."""


def watch_pyramid_from_the_side(characters):
    """String pyramid implementation."""
    container = []
    str_len = len(characters)
    count = str_len + (str_len - 1)
    de_count = count
    if count == 1:
        print(characters)
    while de_count >= 1:
        for item in characters:
            item_count = item * de_count
            container.append(item_count)
            de_count -= 2
    new_container = container[::-1]
    newer_container = []
    for item in new_container:
        concat = (' ' * ((count - len(item)) // 2)) + item + (' ' * ((count - len(item)) // 2)) + '\n'
        newer_container.append(concat)
    return "".join(newer_container)


def watch_pyramid_from_above(alist):
    """String pyramid implementation view from above."""
