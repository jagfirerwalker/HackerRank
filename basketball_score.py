import sys

def getRecord(s):
    hscore = lscore = s[0]
    hcounter = lcounter = 0

    for i in range(len(s)):
        if hscore < s[i]:
            hscore = s[i]
            hcounter += 1
        if lscore > s[i]:
            lscore = s[i]
            lcounter += 1
    return hcounter, lcounter

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

'''
Sample input
10
3 4 21 36 10 28 35 5 24 42

Sample outpu
4 0
'''
