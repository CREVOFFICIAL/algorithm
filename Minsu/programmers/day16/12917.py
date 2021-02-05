# 문자열 내림차순으로 배치하기

def solution(s):
    tmp = sorted(s, reverse=True)
    # print(tmp)
    answer = "".join(tmp)
    # print(answer)
    return answer
