def solution(n):
    # dic = {0: 0, 1: 1}
    # def fibo(n):
    #     if n == 0 or n == 1:
    #         return n
    #     first = dic[n-1] if n-1 in dic else fibo(n-1)
    #     second = dic[n-2] if n-2 in dic else fibo(n-2)
    #     if n not in dic:
    #         dic[n] = (first+second) % 1234567
    #         return dic[n]

    lst = []
    for i in range(0, n+1):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        else:
            lst.append(lst[i-1] + lst[i-2])
    return lst[n] % 1234567

print(solution(5))