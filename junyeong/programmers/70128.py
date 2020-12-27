def solution(a, b):
    answer = 0
    
    for digit in range(len(a)):
        answer += a[digit] * b[digit]
    
    return answer
