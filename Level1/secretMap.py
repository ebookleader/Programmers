def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        combinedMap = bin(arr1[i] | arr2[i])[2:]
        if len(combinedMap) < n:
            combinedMap = '0'*(n-len(combinedMap)) + combinedMap
        answer.append(combinedMap.replace('1', '#').replace('0', ' '))
    return answer

print(solution(6,	[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
