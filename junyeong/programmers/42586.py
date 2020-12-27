import math

def solution(progresses, speeds):
    time = 0
    should_release = True
    answer = []
    # 남은 시간을 구한다.
    
    count = 0
    
    for index, progress in enumerate(progresses):
        if should_release:
            time = max(math.ceil((100 - progresses[index]) / speeds[index]), time)
            should_release = False
            count = 1
        else:
            count += 1
        
        if index+1 < len(progresses):
            work_time = math.ceil((100 - progresses[index+1]) / speeds[index+1])
            if work_time > time:
                answer.append(count)
                should_release = True
            
    answer.append(count)
    return answer
