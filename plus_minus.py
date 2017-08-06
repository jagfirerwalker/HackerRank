import sys


n = int(input("Enter 1 Number: ").strip())
arr = [int(arr_temp) for arr_temp in input("Enter as many space seperated number as previously declared (pos or neg): ").strip().split(' ')]
positive = 0
negative = 0
zero = 0
for i in range(n):
    positive += (1 if arr[i] > 0 else 0)
    negative += (1 if arr[i] < 0 else 0)
    zero += (1 if arr[i] == 0 else 0)
print('{:2f}'.format(positive/n))
print('{:2f}'.format(negative/n))
print('{:2f}'.format(zero/n))


'''
2nd solution

n = float(raw_input())
lst = [int(x) for x in raw_input().split()]
print format(len([x for x in lst if x > 0])/n, ".6f")
print format(len([x for x in lst if x < 0])/n, ".6f")
print format(len([x for x in lst if x == 0])/n, ".6f")

'''
