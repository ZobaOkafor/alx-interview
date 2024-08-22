#!/usr/bin/python3
""" Coin change algorithm. """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list of int): A list of the values of the coins in your possession.
    total (int): The target amount to reach using the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if the total is 0 or less.
         Returns -1 if the total cannot be met by any combination of coins.

    Example:
    >>> makeChange([1, 2, 25], 37)
    7
    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1
    """

    if total <= 0:
        return 0
    else:
        from math import trunc

        coins = sorted(coins, reverse=True)
        coin_dict = {}
        while total is not None:
            for c in coins:
                if total % c == 0:
                    coin_dict[c] = total / c
                    return(int(sum(coin_dict.values())))
                else:
                    coin_dict[c] = trunc(total / float(c))
                    total -= (c * coin_dict[c])
            return -1
