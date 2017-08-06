#!/bin/python3

import sys

def timeConversion(s):
    hour = int(s[:2]) #take first 2 digest from the front
    merridian = s[-2:] #take the last to from the end
    if hour == 12:
        hour = 0
    if merridian == "PM":
        hour += 12
    return ("%02d" % hour + s[2:8])

s = input().strip()
result = timeConversion(s)
print(result)
