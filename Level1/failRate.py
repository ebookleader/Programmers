def solution(N, stages):
    stages.sort()
    dic = {}
    answer = []
    for i in range(1, N+1):
        total = len(stages)
        fail = stages.count(i)
        if total == 0:
            dic[i] = 0
        else:
            dic[i] = (fail/total)
        stages = stages[fail:]
    sortedDic = sorted(dic.items(), key = lambda  x: x[1], reverse=True)
    for s in sortedDic:
        answer.append(s[0])
    return answer

print(solution(7, [2, 1, 2, 6, 2, 4, 3, 3]))