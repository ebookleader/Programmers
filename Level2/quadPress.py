import numpy as np

def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def helper(x, y, n):
        chk = arr[x][y] # 시작점 값
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != chk:
                    s = n // 2
                    helper(x, y, s)
                    helper(x, y+s, s)
                    helper(x+s, y, s)
                    helper(x+s, y+s, s)
                    return
        answer[chk] += 1
    helper(0, 0, n)
    return answer


# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))