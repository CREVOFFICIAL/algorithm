# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):

    result = []

    for i in range(len(arr)):
        cal = arr[i] % divisor
        if cal == 0:
            result.append(arr[i])

    # print(result)
    if len(result) == 0:
        result.append(-1)
    answer = sorted(result)

    # print(answer)
    return answer
