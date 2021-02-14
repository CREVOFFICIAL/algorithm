def solution(n, m):
    number = max(n, m)
    divisor = min(n, m)
    
    while(number % divisor != 0):
        remainder = number % divisor
        number = divisor
        divisor = remainder
        
    return [divisor, n * m // divisor]
