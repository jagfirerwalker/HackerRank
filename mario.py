#!/bin/python3

import sys


n = int(input().strip())

'''
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(n-(n-1)+i):
        print("#", end="")
    print()
'''
[print(' '*(n-i) + '#'*i) for i in range(1,n+1)] #print ' '*(total number - counter) + '#'*counter for counter in range from 1 to total01
[print(("#"*i).rjust(n) ) for i in range(1,n+1)] #print '#'*counter, move previou to right (rjust) by total value
