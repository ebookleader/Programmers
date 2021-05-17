# 1,3,5,7,12
# 1번은 sort로 해결
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    answer = n - len(lost)
    for i in range(len(lost)-1, -1, -1):
        if lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer += 1
        elif lost[i]-1 in reserve:
            reserve.remove((lost[i]-1))
            answer += 1
    return answer

print(solution(5, [2,3,4], [1,2,3]))
