def solution(numbers, hand):
    left = (3, 0)
    right = (3, 2)
    
    answer = ''
    # 3으로 나눴을때 좌표 변환 (몫, 나머지)
    for number in numbers:
        if number == 0:
            pos = (3, 1)
        else:
            pos = ((number - 1) // 3, (number - 1) % 3)
        print(number, pos)
        if pos[1] == 0:
            answer += 'L'
            left = pos
        elif pos[1] == 2:
            answer += 'R'
            right = pos
        else:
            leftDiff = abs(pos[0] - left[0]) + abs(pos[1] - left[1])
            rightDiff = abs(pos[0] - right[0]) + abs(pos[1] - right[1])
            
            if leftDiff < rightDiff:
                answer += 'L'
                left = pos
            elif leftDiff > rightDiff:
                answer += 'R'
                right = pos
            else:
                if hand == "left":
                    answer += 'L'
                    left = pos
                else:
                    answer += 'R'
                    right = pos
    
    return answer
