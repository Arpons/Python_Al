def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(3, 9))

# 유클리드 방식 최대공약수 찾기

def gcgEuclid(a, b):
    if b == 0:
        return a
    return gcgEuclid(b, a % b)

print(gcgEuclid(12, 64))