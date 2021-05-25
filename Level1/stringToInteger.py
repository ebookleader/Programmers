def solution(s):
    if s[0].isdigit():
        s = '+' + s
    sign = s[0]
    answer = int(s[1:])
    if sign == '-':
        answer *= -1
    return answer

print(solution('+1234'))