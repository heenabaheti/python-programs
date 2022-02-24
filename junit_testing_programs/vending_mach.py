"""
A virtual vending machine.
"""
# A list of coins allowed
ACCEPTABLE_COINS = [1000, 500, 200, 100, 20, 10, 5, 2, 1]


def return_change(balance):
    """
    Returns balance in coins.
    """
    change = []

    while balance > 0:
        for coin in ACCEPTABLE_COINS:
            if balance % coin == 0:
                change.append(coin)
                balance -= coin
                break

    return sorted(change, reverse=True)
