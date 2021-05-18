def solution(numbers, hand):
    answer = ''
    L, R = '*', '#'
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    while numbers:
        n = numbers.pop(0)
        touch = ''
        if n in [1, 4, 7]:
            touch = 'L'
            L = n
        elif n in [3, 6, 9]:
            touch = 'R'
            R = n
        else: # 2,5,8,0
            left = [abs(dic[n][0] - dic[L][0]), abs(dic[n][1] - dic[L][1])]
            right = [abs(dic[n][0] - dic[R][0]), abs(dic[n][1] - dic[R][1])]
            leftDist = left[0] + left[1]
            rightDist = right[0] + right[1]
            if leftDist < rightDist:
                touch = 'L'
                L = n
            elif leftDist > rightDist:
                touch = 'R'
                R = n
            else:
                if hand == 'left':
                    touch = 'L'
                    L = n
                else:
                    touch = 'R'
                    R = n
        answer += touch
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))