def solution(arr):
    min_value = min(arr)
    index = arr.index(min_value)
    del arr[index]
    
    if arr:
        return arr
    else:
        return [-1]
