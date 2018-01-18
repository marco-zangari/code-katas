"""Test proper parenthetics."""

import pytest

from proper_parenthetics import lisp_parens_with_count, lisp_parens_with_stack


def test_lisp_parens_with_count_closed():
    """Output with count to see whether parens closed(-1)."""
    input = lisp_parens_with_stack(')))(((')
    assert input == -1


def test_lisp_parens_with_count_open():
    """Output with count to see whether parens open(1)."""
    input = lisp_parens_with_stack('((())')
    assert input == 1


def test_lisp_parens_with_count_balanced():
    """Output with count to see whether parens balanced(0)."""
    input = lisp_parens_with_stack('((()))')
    assert input == 0


def test_lisp_parens_with_stack_start_closed():
    """Output with stack to see whether parens closed(-1)."""
    input = lisp_parens_with_stack(')))(((')
    assert input == -1


def test_list_parens_with_stack_start_open():
    """Output with stack to see whether parens open(1)."""
    input = lisp_parens_with_stack('((())')
    assert input == 1


def test_list_parens_with_stack_start_balanced():
    """Output with stack to see whether parens balanced(0)."""
    input = lisp_parens_with_stack('((()))')
    assert input == 0
