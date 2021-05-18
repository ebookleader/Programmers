from math import sqrt
from itertools import combinations
def solution(nums):
    sum_list = []
    answer = 0

    # 3중 for문 사용하는 방법
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_list.append(nums[i]+nums[j]+nums[k])
    for s in sum_list:
        if checkPrime(s):
            answer += 1

    # itertools 사용하는 방법
    for c in combinations(nums, 3):  # 3개 선택
        threeSum = sum(c)
        if checkPrime(threeSum):
            answer += 1
    return answer

def checkPrime(num) -> bool:
    result = True
    for i in range(2, int(sqrt(num))+1):
        if (num % i) == 0:
            result = False
            break
    return result

print(solution([1,2,7,6,4]))

# 소수 판별 알고리즘
# 1번
def checkPrime1(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True

