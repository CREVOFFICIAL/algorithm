# 내적

def solution(a, b):
    answer = 0
    for item1, item2, in zip(a, b):
        tmp = (item1 * item2)
        answer += tmp
    return answer
