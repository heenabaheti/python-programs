"""
Tests return change
"""
from vending_mach import return_change
from binary_to_decimal import binary_to_decimal
from decimal_hexadecimal import decimal_to_hex


def test_call_with_zero():
    """
    When no balance exists, no coins should be returned.
    """
    assert return_change(0) == []


def test_call_with_265():
    """
    When the balance is 265, a 200, two 20, a 10 and 5 coin
    should be returned.
    """
    assert return_change(265) == [200, 20, 20, 20, 5]


def test_binary_to_deci():
    """
    when the input is 1111
    :return: is decimal no 15
    """
    assert binary_to_decimal(1111) == 15
