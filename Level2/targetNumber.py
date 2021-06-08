def solution(numbers, target):
    answer = [0]
    for i in numbers:
        tmp = []
        for j in answer:
            tmp.append(j+i)
            tmp.append(j-i)
        answer = tmp
    return answer.count(target)

print(solution([1, 1, 1, 1, 1], 3))