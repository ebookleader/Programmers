def solution(new_id: str):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    answer = ''
    for i in range(len(new_id)):
        if new_id[i] in ['-', '_', '.'] or new_id[i].isdigit() or (ord('a') <= ord(new_id[i]) <= ord('z')):
            answer += new_id[i]
    # 3단계
    for i in range(len(answer)-2, -1, -1):
        if answer[i] == '.':
            if answer[i+1] == '.':
                answer = answer[:i] + answer[i+1:]
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) < 3:
        last = answer[-1]
        while len(answer) < 3:
            answer += last
    return answer

print(solution("abcdefghijklmn.p"))
