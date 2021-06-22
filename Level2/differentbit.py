def solution(numbers):
    answer = []
    for n in numbers:
        bitN = bin(n)[2:]
        if n % 2 == 0:  # 짝수
            bitN = bitN[:-1] + '1'
        else:   # 홀수
            # 가장 오른쪽에 잇는 0 찾기 -> 1로 바꿈 -> 다음 자리에 0으로 변경
            if bitN.count('0') == 0:
                bitN = '0' + bitN
            idx = bitN.rfind('0')
            rear = bitN[idx+2:]
            bitN = bitN[:idx] + '10' + rear
        answer.append(int(bitN, 2))
    return answer

print(solution([2, 7]))

