def solution(m, musicinfos):
    answer = ''
    ansList = []

    def changeChar(st):
        i = 0
        tmp = ''
        while i < len(st):
            if st[i] == '#':
                c = tmp[-1].lower()
                tmp = tmp[:-1] + c
            else:
                tmp += st[i]
            i += 1
        return tmp

    # m에서 #음표 소문자 변환
    m = changeChar(m)

    for info in musicinfos:
        # 분리
        info = info.split(',')

        # #음표 소문자로 변환
        info[3] = changeChar(info[3])

        # 재생시간 추가 (min)
        start = info[0].split(':')
        end = info[1].split(':')
        playTime = (int(end[0])*60 + int(end[1])) - (int(start[0])*60 + int(start[1]))
        info.append(playTime)

        # 실제 재생 멜로디 추가
        melody = info[3]
        if playTime < len(melody):
            melody = melody[:playTime]
        else:
            re, mod = divmod(playTime, len(melody))
            melody = melody * re + melody[:mod]
        info.append(melody)

        # 포함 여부 확인
        if m in melody:
            ansList.append(info)

    if len(ansList) == 0:
        answer = '(None)'
    elif len(ansList) == 1:
        answer = ansList[0][2]
    else:
        maxLength = 0
        for ans in ansList:
            if ans[4] > maxLength:
                maxLength = ans[4]
                answer = ans[2]
    return answer

# print(solution('ABCDEFG', ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
