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

    # Sort coins in descending order to prioritize larger denominations
    coins.sort(reverse=True)

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make the total of 0

    # Fill dp array with optimized steps
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

            # Early termination if the exact total is reached with minimal coins
            if dp[total] != float('inf'):
                break

    # If dp[total] is still infinity, no combination could meet the total
    return dp[total] if dp[total] != float('inf') else -1
