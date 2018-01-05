"""Test the string pyramid implementation."""


import pytest

from string_pyramid import watch_pyramid_from_the_side


def test_watch_pyramid_from_the_side_one_char():
    """Test from the side."""
    output = watch_pyramid_from_the_side('a')
    assert output == 'a\n'


def test_watch_pyramid_from_the_side_multiple_char():
    """Test from the side."""
    output = watch_pyramid_from_the_side('abc')
    assert output == '  c  \n bbb \naaaaa\n'
