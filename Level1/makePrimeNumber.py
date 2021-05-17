from math import sqrt
def solution(nums):
    sum_list = []
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_list.append(nums[i]+nums[j]+nums[k])
    for s in sum_list:
        if checkPrime(s):
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