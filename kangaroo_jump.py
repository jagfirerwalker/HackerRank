#!/bin/python3

import sys
'''
def kangaroo(x1, v1, x2, v2):
    k1 = x1
    k2 = x2
    for i in range(1000):
        k1 += v1
        k2 += v2
        if k1 == k2:
            return True
    return False
'''
def kangaroo(x1, v1, x2, v2):
    x, y = sorted([[x1, v1], [x2, v2]], key=lambda el: el[0])
    print(x)
    print(y)
    print(x[0]-y[0])
    print((x[0]-y[0]) % (x[1]-y[1]))
    if not x[1] > y[1] or (x[0]-y[0]) % (x[1]-y[1]):
      return 'NO'
    else:
      return 'YES'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

'''
Test Case
0 3 4 2

x1 + (v1 * n) = x2 + (v2 * n)
We can check this by looking at the sample input 0, 3, 5, 2 for x1, v1, x2, v2 respectively.
0 + 3n = 5 + 2n n = 5
This means it takes the kangaroos jumping 5 times to land at the same distance:
0 > 3 > 6 > 9 > 12 > 15
5 > 7 > 9 > 11 > 13 > 15
Now that we know the equation is right, let's move n to one side:
(v1 * n) - (v2 * n) = x2 - x1
n(v1 - v2) = x2 - x1
n = (x2 - x1) / (v1 - v2)
We don't know what the value of n will be, but we know that it must be an integer. If the division solves for a whole integer, we know there is no remainder value. So, we use modular division
(x2 - x1) % (v1 - v2) == 0 (meaning no remainder value, and therefore the division solves for an integer)

'''
