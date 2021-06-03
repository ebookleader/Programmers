def solution(s):
    s = list(s)
    stack = []

    # for i in s:
    #     stack.append(i)
    #     if len(stack) > 1 and (stack[-1] == stack[-2]):
    #         stack.pop()
    #         stack.pop()

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0


print(solution('abccccbaaa'))

