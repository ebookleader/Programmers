def solution(dirs):
    answer = 0
    x, y = 0, 0
    maxX, maxY, minX, minY = 5, 5, -5, -5
    visit = []
    for d in dirs:
        if d == 'U':
            if y+1 <= maxY:
                bx, by = x, y
                y += 1
        elif d == 'D':
            if y-1 >= minY:
                bx, by = x, y
                y -= 1
        elif d == 'R':
            if x+1 <= maxX:
                bx, by = x, y
                x += 1
        else:
            if x-1 >= minX:
                bx, by = x, y
                x -= 1

        sToe = (bx, by, x, y)
        eTos = (x, y, bx, by)
        if sToe not in visit or eTos not in visit:
            visit.append(sToe)
            visit.append(eTos)
            answer += 1
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDU"))