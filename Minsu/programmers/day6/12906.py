# 같은 숫자는 싫어

def solution(arr):
    answer = []
    l = len(arr)
    for i in range(l):
        # print('l', i)
        # print('arr[i]', arr[i])

        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
