def solution(n, m):

    def gcd(a, b):
        while b != 0:
            k = a % b
            a = b
            b = k
        return a

    def lcm(a, b, g):
        return (a * b) // g

    g = gcd(n, m)
    l = lcm(n, m, g)

    return [g, l]

print(solution(2, 5))