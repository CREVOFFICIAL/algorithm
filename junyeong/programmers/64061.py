def solution(board, moves):
    answer = 0
    stack = []
    missed = 0
    
    for move in moves:
        for depth in range(len(board)):
            if board[depth][move - 1] != 0:
                item = board[depth][move - 1]
                board[depth][move - 1] = 0
                if not stack:
                    stack.append(item)
                else:
                    if stack[-1] == item:
                        stack.pop()
                        missed += 2
                    else:
                        stack.append(item)
                break
    
    return missed
