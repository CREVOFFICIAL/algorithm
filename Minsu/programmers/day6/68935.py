# 3진법 뒤집기

def trans(n):
    ten, three = 0, ''
    while n != 0:
        mod = n % 3
        three += str(mod)
        n = n // 3
    for idx, t in enumerate(three[::-1]):
        ten += ((3 ** idx) * int(t))
    return ten


def solution(n):
    return trans(n)
