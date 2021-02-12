# 평균 구하기

def solution(arr):
    sum = 0
    l = len(arr)
    for i in arr:
        sum += i
    answer = sum / l
    # answer = 0
    return answer
