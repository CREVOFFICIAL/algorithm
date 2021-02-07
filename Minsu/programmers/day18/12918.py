# 문자열 다루기 기본

def solution(s):

    l = len(s)
    return s.isdigit() and (l == 4 or l == 6)
