def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

print(solution([5,9,7,10], 5))