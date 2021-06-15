def solution(msg):
    answer = []
    # 사전 초기화
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = (i+1)

    i = 0
    while i < len(msg):
        tmp = msg[i]
        i += 1
        if i == len(msg):
            answer.append(dic[tmp])
            break
        nxt = tmp + msg[i]
        while nxt in dic:
            tmp = nxt
            i += 1
            if i == len(msg):
                break
            nxt = tmp + msg[i]
        answer.append(dic[tmp])
        dic[nxt] = len(dic) + 1

    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))