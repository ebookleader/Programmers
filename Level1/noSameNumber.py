# def solution(arr):
#     for i in range(len(arr)-1, 0, -1):
#         if arr[i] == arr[i-1]:
#             del arr[i]
#     return arr

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))