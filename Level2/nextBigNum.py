def solution(n):
    oneNum = bin(n)[2:].count('1')
    while True:
        n += 1
        bi = bin(n)[2:].count('1')
        if bi == oneNum:
            break
    return n

print(solution(78))