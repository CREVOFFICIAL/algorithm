def solution(a, b):
    answer = 0
    min_value = min(a, b)
    max_value = max(a, b)
    for value in range(min_value, max_value+1):
        answer += value
    return answer
