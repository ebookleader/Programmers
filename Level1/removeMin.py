def solution(arr):
    answer = []
    arr.remove(min(arr))
    return arr if len(arr) > 0 else [-1]