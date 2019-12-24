def makingOne():
    x = int(input("정수 입력 : "))
    count = 0
    while True : 
        
        if x % 3 == 0:
            x = x / 3
        elif x % 2 == 0:
            x = x / 2
        else:
            x = x - 1
        
        if x == 1:
            break
        count += 1
    return count