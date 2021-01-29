#  h - index

def solution(citations):
    s = citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i

    return 0
