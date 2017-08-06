#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


apples_on_house = oranges_on_house = 0
for i  in apple:
    if s <= (a+i) and t>= (a+i):
        apples_on_house += 1
for i in orange:
    if s <= (b+i) and t>= (b+i):
        oranges_on_house += 1

print(apples_on_house)
print(oranges_on_house)

'''
Alternative Solution

print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

Test Case

7 11
5 15
3 2
-2 2 1
5 -6
'''
