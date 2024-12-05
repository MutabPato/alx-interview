#!/usr/bin/python3
"""Making Change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given amount total

    Args:
        coins (list): List of coin denominations.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed to meet the total,
        or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins needed
    # for each amount up to `total`
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
