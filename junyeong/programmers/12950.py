def solution(arr1, arr2):
    answer = [[a + b for a, b in zip(item1, item2)] for item1, item2 in zip(arr1, arr2)]
    return answer
