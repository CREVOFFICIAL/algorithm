# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    tmp = sorted((a, b))
    print(tmp)

    for i in range(tmp[0], tmp[1]+1):
        # print(i)
        answer += i

    print(answer)
    return answer
