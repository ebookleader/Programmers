def solution(s):
    # s = s.replace('()', '')
    # s = list(s)
    #
    # # 조기 종료 (test2 통과)
    # if s.count('(') != s.count(')'):
    #     return False
    #
    # stack = []
    # while len(s) > 0:
    #     stack.append(s.pop())
    #     if len(stack) > 1 and ''.join(reversed(stack[-2:])) == '()':
    #         stack.pop()
    #         stack.pop()
    # return True if len(stack) == 0 else False
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0

print(solution(")"))