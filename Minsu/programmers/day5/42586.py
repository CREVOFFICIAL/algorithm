# 기능 개발

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    # progresses 길이에 맞게 loop 가 돈다
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
