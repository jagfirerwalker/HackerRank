#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    alice = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
    bob = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
    return (alice, bob)


a0, a1, a2 = [5, 6, 7]
b0, b1, b2 = [3, 6, 10]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
