def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    d = 2

    while d * d <= n:
        while n % d == 0:
            operations += d
            n //= d
        d += 1

    if n > 1:
        operations += n

    return operations
