def solution(num):
    answer = 0
    cnt = 0
    while num > 1 and cnt <= 500:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        cnt += 1
    return cnt if cnt <= 500 else -1

print(solution(626331))