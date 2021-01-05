# 수박수박수

def solution(n):
    answer = ''

    # range?
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer
