from itertools import chain

def solution(n):
    numbers = [[0 for _ in range(n)] for _ in range(n)]
    max_number = sum(i for i in range(1, n+1))
    y, x = -1, 0
    size = n - 1
    
    directions = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
    count = 0
    current = 0
    
    for number in range(1, max_number+1):
        position = directions[current]
        y += position[0]
        x += position[1]
        numbers[y][x] = number
        
        if count < size:
            count += 1
        else:
            count = 0
            size -= 1
            current = (current + 1) % 3
    
    answer = [i for i in chain(*numbers) if i != 0]
    return answer
