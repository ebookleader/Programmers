import collections
def solution(participant, completion):
    # answer = ''
    # dic = {}
    # for p in participant:
    #     if p not in dic:
    #         dic[p] = 1
    #     else:
    #         dic[p] += 1
    # for c in completion:
    #     dic[c] -= 1
    #     if dic[c] == 0:
    #         del dic[c]
    # for key in dic:
    #     if dic[key] > 0:
    #         answer = key
    # return answer
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
