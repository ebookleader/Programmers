def solution(n):
    ans = 1
    while n > 1:
        mod = n % 2
        if mod == 1:    # 점프
            n -= 1
            ans += 1
        else:   # 순간이동
            n //= 2
    return ans

# def solution(n):
#     ans = 1
#     while n > 1:
#         ans += (n % 2)
#         n //= 2
#     return ans

print(solution(5000))