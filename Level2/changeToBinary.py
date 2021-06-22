def solution(s):
    answer = [0, 0] # [변환횟수, 제거된 0의개수]
    while len(s) > 1:
        zero = s.count('0')
        answer[1] += zero
        s = bin(len(s)-zero)[2:]
        answer[0] += 1
    return answer

print(solution("110010101001"))