from itertools import combinations

def issubset2(_min, column): 
    for m in _min:
        m, column = set(m) , set(column)
        if m.issubset(column):
            return True
    return False

def solution(relation):
    union = []
    count = 0
    for index in range(1, len(relation)+1):
        l = list(combinations(list(range(len(relation[0]))), index))
        for item in l:
            if issubset2(union, item):
                continue
            tuples = set()
            for i in range(len(relation)):
                key = "".join([relation[i][v] for v in item])
                tuples.add(key)
            if len(tuples) == len(relation):
                count += 1
                union.append(item)
    return count
