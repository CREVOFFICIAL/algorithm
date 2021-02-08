# 최대공약수와 최소공배수

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    result = x*y // gcd(x, y)
    return result


def solution(n, m):
    value1 = gcd(n, m)
    value2 = lcm(n, m)

    return [value1, value2]
