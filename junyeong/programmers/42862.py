def solution(n, lost, reserve):
    students = dict()
    for number in range(n+2):
        students[number] = 1
        
    union = set(lost) & set(reserve)
    lost_diff = list(set(lost) - union)
    reserve_diff = list(set(reserve) - union)
    
    for number in lost_diff:
        students[number] = 0
    
    for number in sorted(reserve_diff):
        if students[number-1] == 0:
            students[number-1] = 1
        elif students[number+1] == 0:
            students[number+1] = 1
            
    answer = sum(students.values()) - 2
    return answer
