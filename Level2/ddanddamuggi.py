def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
    return max(land[-1])

    # for i in range(len(land)-2, -1, -1):
    #     land[i][0] += max(land[i + 1][1], land[i + 1][2], land[i + 1][3])
    #     land[i][1] += max(land[i + 1][0], land[i + 1][2], land[i + 1][3])
    #     land[i][2] += max(land[i + 1][0], land[i + 1][1], land[i + 1][3])
    #     land[i][3] += max(land[i + 1][0], land[i + 1][1], land[i + 1][2])
    # return max(land[0])

print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))