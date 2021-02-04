# 정수 제곱근 판별

import math


def solution(n):
    tmp = (math.sqrt(n))
    itmp = int(tmp)

    if (tmp == itmp):
        answer = (tmp+1) * (tmp+1)
        return answer
    else:
        return -1
