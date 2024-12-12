#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    """
    def sieve(n):
        """
        Helper function to generate primes using the sieve of Eratosthenes
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * 1, n + 1, i):
                    primes[j] = False
        return primes

    # Precomputing primes up to the largest number in nums
    max_num = max(nums)
    primes = sieve(max_num)

    # Creating a list to count the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Maria wins if the number of primes up to n is odd, otherwise Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins + 1
        else:
            ben_wins += 1

        # Determine the overall winner
        if maria_wins > ben_wins:
            return "Maria"
        elif ben_wins > maria_wins:
            return "Ben"
        else:
            return None
