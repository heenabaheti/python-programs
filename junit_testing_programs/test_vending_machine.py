"""
Tests return change
"""

from vending_mach import return_change
from binary_to_decimal import binary_to_decimal
from binary_to_decimal import decimal_to_binary
# from monthly_payment import monthly_payment
from square_root_newton import SquareRoot


def test_call_with_zero():
    # testing for vending machine program
    """
    When no balance exists, no coins should be returned.
    """
    assert return_change(0) == []


def test_call_with_265():
    # testing for vending machine program
    """
    When the balance is 265, a 200, two 20, a 10 and 5 coin
    should be returned.
    """
    assert return_change(265) == [200, 20, 20, 20, 5]


def test_binary():
    """
    when the input is 1111 result is 15
    """
    assert binary_to_decimal(1111) == str(15)


def test_decimal():
    """
    when the input is 15 result is 1111
    """
    assert decimal_to_binary(15) == str(1111)


""" def test_monthly():
 assert monthly_payment(12, 1, 12000) == float(135.219)"""


def test_square():
    assert SquareRoot.square_root(12) == 3.464101615137755
