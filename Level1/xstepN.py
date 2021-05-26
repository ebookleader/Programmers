def solution(x, n):
    answer = []
    step = x
    for _ in range(n):
        answer.append(x)
        x += step
    return answer

print(solution(2, 5))