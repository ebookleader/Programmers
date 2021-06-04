from collections import deque

# 큐에 넣고 덧셈 진행한다음에 100이되면 앞에서부터 빼주기
def solution(progresses, speeds):
    answer = []
    # deq = deque([progresses[i], speeds[i]] for i in range(len(progresses)))
    # while deq:
    #     cnt = 0
    #     for i in range(len(deq)):
    #         if deq[i][0] >= 100:
    #             continue
    #         else:
    #             deq[i][0] += deq[i][1]
    #     while deq[0][0] >= 100:
    #         cnt += 1
    #         deq.popleft()
    #         if not deq:
    #             break
    #     if cnt > 0:
    #         answer.append(cnt)
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    day = 0
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))