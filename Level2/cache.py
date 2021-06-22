from collections import deque

def solution(cacheSize, cities):

    answer = 0
    queue = deque(maxlen=cacheSize)
    cities = deque(cities)
    miss, hit = 5, 1

    if cacheSize == 0:
        return len(cities) * miss

    while len(cities) > 0:
        city = (cities.popleft()).lower()
        if city in queue:
            answer += hit
            queue.remove(city)
        else:
            answer += miss
            if len(queue) >= cacheSize:
                queue.pop()
        queue.appendleft(city)

    return answer

print(solution(	1, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(5, ['Seoul', 'Seoul', 'Seoul']))