"""Test the string pyramid implementation."""


import pytest

from string_pyramid import watch_pyramid_from_the_side, watch_pyramid_from_above


def test_watch_pyramid_from_the_side_one_char():
    """Test from the side."""
    output = watch_pyramid_from_the_side('a')
    assert output == 'a\n'


def test_watch_pyramid_from_the_side_multiple_char():
    """Test from the side produces side profile."""
    output = watch_pyramid_from_the_side('abc')
    assert output == '  c  \n bbb \naaaaa\n'


def test_watch_pyramid_from_above():
    """Test from above produces grid output."""
    output = watch_pyramid_from_above('abc')
    assert output == [['a', 'a', 'a', 'a', 'a'], ['a', 'b', 'b', 'b', 'a'],
 ['a', 'b', 'c', 'b', 'a'],
 ['a', 'b', 'b', 'b', 'a'],
 ['a', 'a', 'a', 'a', 'a']]


def test_count_visible_characters_of_the_pyramid():
    """Test whether count of visible characters works."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    output = count_visible_characters_of_the_pyramid('abcde')
    assert output == 81


def test_count_all_characters_of_the_pyramid(characters):
    """Test whether count picks up all characters visible, invisible."""
    from string_pyramid import count_all_characters_of_the_pyramid
    output = count_all_characters_of_the_pyramid('abcde')
    assert output == 165