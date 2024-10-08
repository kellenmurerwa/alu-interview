#!/usr/bin/python3
"""mini operations"""


def minOperations(n):
    if n <= 1:
        return 0

    oprtns = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            oprtns += divisor
            n = n // divisor
        else:
            divisor += 1

    return oprtns
