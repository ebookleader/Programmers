# def solution(record):
#     answer = []
#     result = []
#     record = [r.split(' ') for r in record]
#     for rec in record:
#         if len(answer) == 0:
#             answer.append(rec)
#         else:
#             if rec[0] == 'Enter':
#                 for ans in answer:
#                     if ans[0] == 'Enter' and rec[1] == ans[1]:
#                         ans[2] = rec[2]
#                         break
#                 answer.append(rec)
#             elif rec[0] == 'Leave':
#                 answer.append(rec)
#             else: # Change
#                 for ans in answer:
#                     if rec[1] == ans[1]:
#                         ans[2] = rec[2]
#     uid = []
#     name = []
#     for ans in answer:
#         if ans[0] == 'Enter':
#             if ans[1] not in uid:
#                 uid.append(ans[1])
#                 name.append(ans[2])
#             result.append(ans[2]+'님이 들어왔습니다.')
#         elif ans[0] == 'Leave':
#             idx = uid.index(ans[1])
#             result.append(name[idx]+'님이 나갔습니다.')
#     return result
def solution(record):
    answer = []
    record = [rec.split(' ') for rec in record]
    dic = {}
    for rec in record:
        if rec[0] != 'Leave':
            dic[rec[1]] = rec[2]
    for rec in record:
        if rec[0] == 'Enter':
            answer.append(dic[rec[1]]+'님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            answer.append(dic[rec[1]]+'님이 나갔습니다.')

    return answer
print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan",
                "Enter uid7777 Cake"]))