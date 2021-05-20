def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = _divsosr(i)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def _divsosr(num):
    result = 0
    for i in range(1, int(num ** 0.5)+1):
        if num % i == 0:
            if i * i == num:
                result += 1
            else:
                result += 2
    return result

print(solution(13, 17))