def fact1(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
def fact2(n):
     if n <= 1:
         return 1
     return n * fact2(n - 1)

def fact3(n):
    if n<= 1:
        return 1
    return n * fact3(n - 1)

print(fact1(3))
print(fact1(5))
print(fact1(6))
print(fact2(3))
print(fact2(5))
print(fact2(6))
print(fact3(1))
print(fact3(3))