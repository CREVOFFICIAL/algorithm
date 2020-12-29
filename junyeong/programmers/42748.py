def solution(array, commands):
    answer = []
    for command in commands:
        number = sorted(array[command[0]-1:command[1]])[command[2]-1]
        answer.append(number)
    return answer
