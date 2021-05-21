def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    dart = ['10' if i == 'k' else i for i in dartResult]

    bonusDic = {'S': 1, 'D': 2, 'T': 3}
    i = -1
    for d in dart:
        if d in bonusDic:
            answer[i] = answer[i] ** bonusDic[d]
        elif d == '*':
            answer[i] *= 2
            if i > 0:
                answer[i-1] *= 2
        elif d == '#':
            answer[i] *= -1
        else: # score인 경우
            answer.append(int(d))
            i += 1

    return sum(answer)
    # dartResult = list(dartResult)
    # score, bonus, option, result = [], [], [], []
    # bonusDic ={'S': 1, 'D': 2, 'T': 3}
    # i = 0
    # while dartResult:
    #     p = dartResult.pop(0)
    #     if i % 3 == 2: # option
    #         if p in ['*', '#']:
    #             option.append(p)
    #         else:
    #             option.append('@')
    #             i += 1
    #     if p.isdigit():
    #         score.append(int(p))
    #         if dartResult[0] == '0':
    #             dartResult.pop(0)
    #             score[-1] *= 10
    #     elif p.isalpha():
    #         bonus.append(bonusDic[p])
    #     i += 1
    #
    # if len(option) < 3:
    #     option.append('@')
    #
    # for i in range(3):
    #     result.append(score[i] ** bonus[i])
    #
    # for i in range(3):
    #     if option[i] == '#':
    #         result[i] *= -1
    #     elif option[i] == '*':
    #         result[i] *= 2
    #         if i > 0:
    #             result[i-1] *= 2
    #
    # return sum(result)

print(solution('1D2S#10S'))
