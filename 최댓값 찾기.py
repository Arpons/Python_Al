import math 

a = [17, 92, 18, 33, 58, 7, 33, 42]

def findMax(a):
    n = len(a)
    maxValue = a[0]
    location = 0
    for i in range(1, n):
        if a[i] > maxValue:
            maxValue = a[i]     #최댓값 
            location = i        #최댓값의 위치
    return maxValue, location
print(findMax(a))

         


