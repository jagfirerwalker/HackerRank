def solution(input):
     p = (input[len(input)-1] - input[0]) / len(input)
     print((input[len(input)-1] - input[0]) )
     print(p)
     for i in range(0, len(input)):
         if(input[i]+p != input[i+1]):
             return input[i]+p
print (solution([1,2,4]))
