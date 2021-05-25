def solution(n):
    prime = []
    prime.append(2)
    if n == 2:
        return 1
    prime.append(3)

    for n in range(5, n+1, 2):
        i = 1
        while prime[i] * prime[i] <= n:
            if n % prime[i] == 0:
                break
            i += 1
        else:
            prime.append(n)
    return len(prime)

print(solution(3))