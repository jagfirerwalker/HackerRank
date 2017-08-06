'''
Colleen is turning n years old! Therefore, she has n candles of various heights on her cake, and candle i has height - i . Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height - i for each individual candle, find and print the number of candles she can successfully blow out.
'''

import sys
'''
Solution 1

def birthdayCakeCandles(n, ar):
    max = 0
    temp = 0
    for i in ar:
        if i > max:
            max = i
    temp = ar.count(max)
    return temp

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

result = birthdayCakeCandles(n, ar)
print(result)
'''

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
print(ar.count(max(ar))) #same soluiton above just condense
