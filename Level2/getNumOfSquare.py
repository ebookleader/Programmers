def solution(w,h):
    answer = 1
    square = gcd(w, h)
    # num = (w // square) + (h // square) - 1
    return (w * h) - (w + h - square)

def gcd(a, b):
    while b != 0:
        k = a % b
        a = b
        b = k
    return a
    

print(solution(8, 12))