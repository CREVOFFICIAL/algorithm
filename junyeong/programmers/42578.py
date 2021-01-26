def solution(clothes):
    closet = dict()
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    answer = 1
    for c in closet.values():
        answer *= (len(c) + 1)
        
    answer -= 1
    return answer
