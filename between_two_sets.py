#!/bin/python3

import sys

def getTotalX(a, b):
    counter = 0
    for i in range(min(a),max(b)+1):
        if all(i % eachA == 0 for eachA in a) and all(eachB % i == 0 for eachB in b):
            counter += 1
    return counter



if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)



'''
Sample Input
2 3
2 4
16 32 96
'''
