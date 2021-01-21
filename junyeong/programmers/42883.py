def solution(number, k):
    answer = ''
    for i in number:
        while len(answer) > 0 and int(answer[-1]) < int(i) and k > 0:
            k -= 1
            answer = answer[:-1]
        answer += i
        
    if k > 0:
        answer = answer[:-k]
    return answer
