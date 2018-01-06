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


def watch_pyramid_from_above(characters):
    """String pyramid implementation view from above."""
    str_len = len(characters)
    count = str_len + (str_len - 1)
    container = []
    max_count = count
    min_count = 0
    if count == 1:
        print(characters)
    for num in range(count):
        char = characters[0] * count
        container.append(list(char))
    max_count -= 1
    min_count += 1
    count -= 2
    while count > 0:
        for ch in characters[1:]:
            for alist in container[min_count: max_count]:
                alist[min_count: max_count] = ch * count
            max_count -= 1
            min_count += 1
            count -= 2
    return container


def count_visible_characters_of_the_pyramid(characters):
    """String count."""
    str_len = len(characters)
    count = str_len + (str_len - 1)
    return count ** 2


def count_all_characters_of_the_pyramid(characters):
    """Count all characters."""
    character_count = 0
    size = len(characters)
    while size > 0:
        size_more = (size + (size - 1)) ** 2
        character_count += size_more
        size -= 1
    return character_count
