def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            cnt1 += 1
        if answers[i] == second[i%len(second)]:
            cnt2 += 1
        if answers[i] == third[i%len(third)]:
            cnt3 += 1

    maxi = max(cnt1, cnt2, cnt3)
    if cnt1 == maxi:
        answer.append(1)
    if cnt2 == maxi:
        answer.append(2)
    if cnt3 == maxi:
        answer.append(3)
    return answer

print(solution([1,3,2,4,2]))

