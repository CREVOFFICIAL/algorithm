def solution(N, stages):
    numbers = {}
    
    for i in range(1, N+1):
        numbers[i] = 0
    
    remains = len(stages)
    for stage in stages:
        if stage != N+1:
            numbers[stage] += 1
            
    fails = []
    
    for i in range(1, N+1):
        if remains == 0:
            fails.append((0, i))
        else:
            fails.append((numbers[i] / remains, i))
            remains = remains - numbers[i]
    
    f = sorted(fails, key = lambda x: (-x[0], x[1]))
    
    answer = []
    for n in f:
        answer.append(n[1])
        
    return answer
