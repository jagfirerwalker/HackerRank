#!/bin/python3
'''
Input
3
11 2 4
4 5 6
10 8 -12

Example output
['11', '2', '4'] 0
7 11 4
['4', '5', '6'] 1
7 5 5
['10', '8', '-12'] 2
-15 -12 10
15

'''
import sys

print('Enter a Number: ', end='')
n = int(input().strip()) #get the total size of NxN matric
total = 0 #set total variable
for i in range(n):
    print('Enter', n, 'number with spaces in between: ', end='')
    row = input().split() #get row input
    total += int(row[i])-int(row[-(i+1)]) #take the i position and substract i+1 position, itereate over till finished
print(abs(total))
