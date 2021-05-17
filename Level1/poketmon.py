def solution(nums):
    answer = 0
    nums.sort()
    lst = list(set(nums))
    if len(lst) > (len(nums)//2):
        answer = (len(nums) // 2)
    else:
        answer = len(lst)
    return answer

print(solution([3,1,2,3]))