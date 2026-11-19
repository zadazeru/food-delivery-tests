import pytest
from cart import cart_total


def test_cart_total_simple():
    assert cart_total([100, 50]) == 150


def test_cart_total_empty():
    assert cart_total([]) == 0


def test_cart_total_with_discount():
    assert cart_total([100, 100], discount=10) == 180


def test_cart_total_negative_price():
    with pytest.raises(ValueError):
        cart_total([-5])


def test_cart_total_full_discount():
    assert cart_total([100, 50], discount=100) == 0


def test_cart_total_zero_discount():
    assert cart_total([100, 50], discount=0) == 150


def test_cart_total_discount_above_100():
    with pytest.raises(ValueError):
        cart_total([100], discount=101)


def test_cart_total_negative_discount():
    with pytest.raises(ValueError):
        cart_total([100], discount=-1)


def test_cart_total_non_numeric_price():
    with pytest.raises(ValueError):
        cart_total(["abc"])


def test_cart_total_rounding():
    assert cart_total([19.99, 10.01], discount=33) == 20.1
