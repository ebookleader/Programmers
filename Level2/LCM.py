from collections import deque

def solution(arr):

    arr = deque(arr)

    def getGcd(a, b):
        while b != 0:
            k = a % b
            a = b
            b = k
        return a

    while len(arr) > 1:
        n = arr.popleft()
        m = arr.popleft()
        gcd = getGcd(n, m)
        lcm = (n * m) // gcd
        arr.append(lcm)

    return lcm

print(solution([2, 6, 8, 14]))