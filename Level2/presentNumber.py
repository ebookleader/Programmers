def solution(n):
    # 연속한 자연수로 표현
    answer = 0
    for i in range(1, n+1):
        num = i
        total = 0
        while True:
            total += num
            if total == n:
                answer += 1
                break
            elif total > n:
                break
            num += 1
    return answer

print(solution(15))