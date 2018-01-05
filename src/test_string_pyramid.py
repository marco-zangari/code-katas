"""Test the string pyramid implementation."""


import pytest

from string_pyramid import watch_pyramid_from_the_side


def test_watch_pyramid_from_the_side():
    """Test from the side."""
    output = watch_pyramid_from_the_side('abc')
    assert output = '  c  \n bbb \naaaaa'
