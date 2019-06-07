def total(n):
    k =  (n * (n + 1)) / 2
    return k

def sum(n):
    s = 0
    for i in range(1, n + 1):    # for 범위 (1부터 n+1까지)
        s = s + i
    return s

print(total(100))
print(sum(100))
