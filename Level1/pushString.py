def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
            continue
        asci = ord(c) + n
        if (ord(c) <= ord('Z')) and (asci > ord('Z')): # 대문자
            asci = ord('A') + (n - (ord('Z') - ord(c)) - 1)
        elif (ord(c) <= ord('z')) and (asci > ord('z')): # 소문자
            asci = ord('a') + (n - (ord('z') - ord(c)) - 1)
        answer += chr(asci)
    return answer

print(solution('z', 1))
print(solution('AB', 1))
print(solution('a Y y', 4))