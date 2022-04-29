#!/usr/bin/env python3
"""method that calculates the fewest number of operations needed
to result in exactly n H characters in the file."""


def minOperations(n):
    """Returns an integer
    If n is impossible to achieve, return 0"""
    numop = 0 '''number operations'''
    x = 2
    while n > 1:
        while n % x == 0:
            numop += x
            n /= x
        x += 1
    return numop
