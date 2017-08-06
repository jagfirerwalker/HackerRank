import sys

arr = list(map(int, input().strip().split(' ')))
min = sys.maxsize-1
max = 0
temp = 0

for i in arr:
    temp += i
    if i > max:
        max = i
    if i < min:
        min = i
print(temp-max, temp-min)
