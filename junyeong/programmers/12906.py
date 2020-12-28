def solution(arr):
    stack = []
    answer = []
    
    for item in arr:
        if not stack:
            stack.append(item)
        else:
            number = stack.pop()
            if number != item:
                answer.append(number)
            stack.append(item)
    
    answer.append(stack.pop())
    return answer
