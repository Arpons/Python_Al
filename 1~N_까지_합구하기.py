def total(n):                       # O(1) : 필요한 계산 횟수가 입력 크기n 과 무관할때 
    k =  (n * (n + 1)) / 2
    return k

def sum(n):                         # O(n) : 필요한 계산 횟수가 입력 크기n 과 비례할때
    s = 0
    for i in range(1, n + 1):       # for 범위 (1부터 n+1까지)
        s = s + i
    return s

print(total(100))
print(sum(100))
