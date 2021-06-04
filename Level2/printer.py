from collections import deque

def solution(priorities, location):
    answer = 0
    idx = location

    priorities = deque(priorities)

    while priorities:
        if priorities[0] == max(priorities):
            answer += 1
            if idx == 0:
                break
            priorities.popleft()
            idx -= 1
        else:
            num = priorities.popleft()
            priorities.append(num)
            idx -= 1
            if idx < 0:
                idx = len(priorities) - 1

    return answer

print(solution([2, 1, 3, 2], 2))