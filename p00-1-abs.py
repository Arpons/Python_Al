import math              #math 모듈 사용

def abs_sign(a):         # 절댓값 구하기
    if a>= 0:
        return a
    else:
        return -a 

def abs_square(a):       # 제곱근 함수 사용
    b = a * a
    return math.sqrt(b)

print(abs_sign(-3))
print(abs_sign(5))
print(abs_square(-3))
print(abs_square(5))