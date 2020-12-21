def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    # n 진법
    # t 출력해야할 갯수
    # m 게임에 참가하는 인원
    # p 튜브의 순서

    numbers = []
    count = t * m
    
    for number in range(count):
        c = list(str(convert(number, n)))
        for s in c:
            numbers.append(s)
    
    answer = ''.join(numbers[p-1::m][:t])
    return answer
