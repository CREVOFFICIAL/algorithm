def solution(n):
    answer = ''
    numbers = ['4', '1', '2']
    
    while (n > 0):
        answer = numbers[n % 3] + answer
        if n % 3 == 0:
            n = n // 3
            n -= 1
        else:
            n = n // 3
    
    return answer
