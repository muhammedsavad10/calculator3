"""Tests for calculator."""

from app import add, subtract, multiply, divide


def test_add():
    """Test add."""
    assert add(2, 3) == 5


def test_subtract():
    """Test subtract."""
    assert subtract(10, 5) == 5


def test_multiply():
    """Test multiply."""
    assert multiply(2, 4) == 8


def test_divide():
    """Test divide."""
    assert divide(8, 2) == 4


def test_divide_float():
    """Test float division."""
    assert divide(5, 2) == 2.5