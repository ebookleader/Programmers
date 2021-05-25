def solution(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    divisor = list(set(divisor))
    return sum(divisor)

print(solution(12))