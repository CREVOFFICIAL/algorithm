# 파일명 정렬

import re


def solution(files):

    # for s in files:
    #     print(s)

    #     파이썬 정규 표현식 작성시
    # ([0-9]+) : 0~9까지의 숫자 반복을 찾는다
    # 파이썬 prefix 는 ra"넣고싶은 정규표현식" 이다

    tmp = [re.split(r"([0-9]+)", s) for s in files]
    # print(tmp)

    sort = sorted(tmp, key=lambda x: (x[0].lower(), int(x[1])))
    # print(sort)

    answer = ["".join(s) for s in sort]
    # print(answer)
    return answer
