def solution(participant, completion):
    answer = ''
    pt = dict()
    
    for i in participant:
        pt[i] = pt.get(i, 0) + 1
    
    for c in completion:
        pt[c] -= 1
    
    for (key, value) in pt.items():
        if value > 0:
            answer = key
    
    return answer
