# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    # print(n)
    # zip : object 를 만들어주는 내장 함수
    for num1, num2, in zip(arr1, arr2):
      #  bin() 해당 값을 바이너리로 표현
      # [start : middle : end] : slice 내장함수 표현
        tmp = bin(num1 | num2)[2:]
        # print('tmp', tmp)
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
            # print('if', tmp)
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer
