def solution(arr, divisor):
    answer = list(filter(lambda element: element % divisor == 0, arr))
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
