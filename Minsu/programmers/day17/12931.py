# 자릿수 더하기

def solution(n):
    l = list(str(n))
    length = len(l)
    answer = 0
    for i in range(length):
        # print(i)
        answer += int(l[i])

    # print(answer)
    return answer
