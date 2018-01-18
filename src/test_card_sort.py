"""Test for card_sort."""

from card_sort import sort_cards
import pytest


def test_sort_cards_1():
    """Test one for card_sort."""
    assert sort_cards(list('39A5T824Q7J6K')) == list('A23456789TJQK')


def test_sort_cards_2():
    """Test two for card_sort."""
    assert sort_cards(list('Q286JK395A47T')) == list('A23456789TJQK')


def test_sort_cards_3():
    """Test three for card_sort."""
    assert sort_cards(list('54TQKJ69327A8')) == list('A23456789TJQK')
