# 메뉴 리뉴얼

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # print(order)
            combi = combinations(sorted(order), c)
            temp += combi
        # print(temp)
        counter = Counter(temp)
        # print(counter)
        # print(counter.values())
        # print(counter.keys())

        # 주문을 안한사람 과 1개만 한 사람은 제외
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f]
                       == max(counter.values())]

    return sorted(answer)
