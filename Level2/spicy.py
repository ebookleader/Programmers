# maxheap으로 해결
import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) # 힙으로 바꿔줌

    while len(scoville) >= 2:
        if scoville[0] < k:
            n = heapq.heappop(scoville)
            m = heapq.heappop(scoville)
            heapq.heappush(scoville, n+m*2)
            answer += 1
        if scoville[0] >= k:
            break
    # 1, 3, 8, 14 해결
    if scoville[0] < k:
        answer = -1
    return answer

print(solution([0, 0, 0, 0], 7))