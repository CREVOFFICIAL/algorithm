def solution(n):
    answer = 0
    number = ''
    
    while(n>=3):
        number = str(n % 3) + number
        n = n // 3
    number = str(n) + number
    number = ''.join(reversed(number))
    
    for index in range(len(number)):
        answer += int(number[index]) * pow(3, len(number) - index - 1)
    
    return answer
