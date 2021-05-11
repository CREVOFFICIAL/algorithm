def solution(land):
    for index, rows in enumerate(land):
        if index == 0:
            continue
        prev_rows = land[index-1]
        rows[0] += max(prev_rows[1], prev_rows[2], prev_rows[3])
        rows[1] += max(prev_rows[0], prev_rows[2], prev_rows[3])
        rows[2] += max(prev_rows[0], prev_rows[1], prev_rows[3])
        rows[3] += max(prev_rows[0], prev_rows[1], prev_rows[2])
        
    return max(land[-1])
