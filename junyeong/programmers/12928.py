def solution(n):
    answer = 0
    for number in range(1,n+1):
        if n % number == 0:
            answer += number
    return answer
