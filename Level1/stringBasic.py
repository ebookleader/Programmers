def solution(s):
    # answer = True
    # if len(s) == 4 or len(s) == 6:
    #     for c in s:
    #         if not c.isdigit():
    #             answer = False
    #             break
    # else:
    #     answer = False
    # return answer

    return s.isdigit() and len(s) in [4, 6]