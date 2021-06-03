import sys
def solution(s):

    if len(s) == 1:
        return 1

    answer = sys.maxsize

    for i in range(1, len(s)//2 + 1): # 자르는 개수
        txt = ''
        cnt = 1
        word = s[0:i]
        for j in range(i, len(s)+i, i):
            if word == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    txt = txt + str(cnt) + word
                else:
                    txt += word
                word = s[j:j+i]
                cnt = 1
        answer = min(answer, len(txt))
    return answer

print(solution('a'))