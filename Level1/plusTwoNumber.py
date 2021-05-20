from itertools import combinations
def solution(numbers):
    answer = []
    combination = combinations(numbers, 2)
    for c in combination:
        if sum(c) not in answer:
            answer.append(sum(c))
    answer.sort()
    return answer