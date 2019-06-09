def findSamename(a):
    n = len(a)                      
    result1 = set()                 # 결과를 저장할 빈 리스트
    for i in range (0, n-1):
        for j in range(i + 1, n):
           if a[i] == a[j]:
               result1.add(a[i])
    return result1

def matchName(a):
    n = len(a)
    
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                print(a[i], a[j])
    return 

b = ["HA","HO", "HI", "HO"]
c = ["HA","HO", "HI"]

print(findSamename(b))   
print(matchName(c))
            