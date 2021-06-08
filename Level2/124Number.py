def solution(n):
    answer = ''
    while n != 0:
        remainder = (n % 3)
        n //= 3
        if remainder == 0: # 3의 배수
            answer += '4'
            n -= 1
        elif remainder == 1:
            answer += '1'
        elif remainder == 2:
            answer += '2'
    return answer[::-1]

for i in range(1, 16):
    print(solution(i))