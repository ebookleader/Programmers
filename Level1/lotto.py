def solution(lottos, win_nums):
    mini = 0
    zero = lottos.count(0)
    for l in lottos:
        if l > 0 and l in win_nums:
            mini += 1
    maxi = (mini + zero)
    answer = [(7-maxi) if maxi > 1 else 6, (7-mini) if mini > 1 else 6]
    return answer