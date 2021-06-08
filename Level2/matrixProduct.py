import numpy as np

def solution(arr1, arr2):
    answer = []
    n, l, m = len(arr1), len(arr2), len(arr2[0])
    print(n, l, m)
    for i in range(n):
        lst = []
        for j in range(m):
            total = 0
            for k in range(l):
                res = arr1[i][k] * arr2[k][j]
                total += res
            print(total)
            lst.append(total)

        answer.append(lst)
    return answer



print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]]))