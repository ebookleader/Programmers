def solution(s):
    answer = []
    lst = s.split(' ')
    for l in lst:
        st = ''
        for i in range(len(l)):
            if i % 2 == 0:
                st += l[i].upper()
            else:
                st += l[i].lower()
        answer.append(st)
    return " ".join(answer)

print(f'"{solution("try hello world")}"')