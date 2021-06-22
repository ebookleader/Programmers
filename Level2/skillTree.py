from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        stack = deque(skill)
        tree = deque(skill_trees[i])
        ans = True
        while tree:
            t = tree.popleft()
            if t in stack:
                s = stack.popleft()
                if s == t:
                    continue
                else:
                    ans = False
                    break
        if ans:
            answer += 1

    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution('CBD',['CED']))