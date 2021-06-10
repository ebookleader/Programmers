def solution(A,B):
    # answer = 0
    # A.sort() # 오름차순
    # B.sort(reverse=True) # 내림차순
    # while A:
    #     answer = answer + (A.pop() * B.pop())
    # return answer

    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))

print(solution([1, 4, 2], [5, 4, 4]))