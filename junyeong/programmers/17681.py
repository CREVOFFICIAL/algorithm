def solution(n, arr1, arr2):
    secret_map = []
    
    for index in range(len(arr1)):
        number = arr1[index] | arr2[index]
        item = bin(number)[2:][-n:].zfill(n)
        map_item = item.replace('1', '#').replace('0', ' ')
        secret_map.append(map_item)
    
    return secret_map
