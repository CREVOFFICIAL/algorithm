def solution(prices):
    answer = [0] * len(prices)
    index = 0
    
    for price in prices:
        for j in range(index+1, len(prices)):
            answer[index] += 1
            if price > prices[j]:
                break
        index += 1
    return answer
