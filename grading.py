#!/bin/python3

import sys

def solve(grades):
    final_grade = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += (5 - i % 5)
            final_grade.append(i)
        final_grade.append(i)
    return final_grade

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
