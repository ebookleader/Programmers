def solution(d, budget):
    lst = []
    d.sort()
    answer = 0
    while sum(lst) <= budget:
        if d:
            lst.append(d.pop(0))
        else:
            answer = len(lst)
            break
    if answer == 0:
        answer = len(lst)-1
    return answer

print(solution([2,2,3,3], 10))