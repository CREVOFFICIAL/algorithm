# 서울에서 김서방 찾기

def solution(seoul):
    # print(seoul)
    answer = []
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer.append(seoul[i])
            answer.append(i)

    # print('asdf', answer[1])
    test = '김서방은 {}에 있다'.format(answer[1])
    return test
    # test = '김서방은'+ answer[1]+ "에 있다"
    # return test
