# 타겟 넘버
# dfs, bfs
def solution(numbers, target):
    a = [0]

    for i in numbers:
        # print(i)
        b = []
        for j in a:
            b.append(j+i)
            b.append(j-i)
            # print(b)
        a = b
    return a.count(target)
