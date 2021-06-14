def solution(n, t, m, p):
    # n: 진법, t: 대답해야하는숫자갯수, m: 참가인원, p: 내 순서
    answer = ''
    ansList = ['0']
    dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
           9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(1, m * t):
        tmp = ''
        while i > 0:
            i, r = divmod(i, n)
            tmp += dic[r]
        ansList.append(tmp[::-1])

    ansList = ''.join(ansList)
    i = 0
    while len(answer) < t:
        answer += ansList[(i * m) + (p - 1)]
        i += 1
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))