def solution(s):
    answer = ''
    count = 0
    
    for char in s:
        if char.isalpha():
            answer += char.upper() if count % 2 == 0 else char.lower()
            count += 1
        else:
            answer += char
            count = 0
            
    return answer
