def solution(x):
    divisor = 0
    n = x
    while n > 0:
        divisor += n % 10
        n = n // 10
    return x % divisor == 0