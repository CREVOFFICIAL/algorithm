# 문자열 내 p와 y의 개수

def solution(s):
    _list = list(s)
    pcnt = 0
    ycnt = 0
    answer = True
    for v in _list:
        lower = v.lower()
        if (lower == 'p'):
            pcnt += 1
        elif(lower == 'y'):
            ycnt += 1

    if (pcnt == ycnt):
        answer = True
    else:
        answer = False

    return answer
