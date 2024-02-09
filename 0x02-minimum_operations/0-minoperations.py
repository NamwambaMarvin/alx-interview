#!/usr/bin/python3


"""
    Read readme.md for instructions
"""


def minOperations(n):
    nOperator = 0
    minOperator = 2
    while n > 1:
        while n % minOperator == 0:
            nOperator += minOperator
            n /= minOperator
        minOperator += 1
    return nOperator
