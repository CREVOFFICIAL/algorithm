def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer_size = len(answers)
    result = []
    
    if answer_size > len(supo1):
        size = answer_size - len(supo1)
        q = answer_size // len(supo1)
        r = answer_size % len(supo1)
        supo1 = supo1 * q + supo1[:r]
    if answer_size > len(supo2):
        size = answer_size - len(supo2)
        q = answer_size // len(supo2)
        r = answer_size % len(supo2)
        supo2 = supo2 * q + supo2[:r]
    if answer_size > len(supo3):
        size = answer_size - len(supo3)
        q = answer_size // len(supo3)
        r = answer_size % len(supo3)
        supo3 = supo3 * q + supo3[:r]
    
    count = {1: 0, 2: 0, 3: 0}
    
    for index in range(len(answers)):
        if answers[index] == supo1[index]:
            count[1] += 1
        if answers[index] == supo2[index]:
            count[2] += 1
        if answers[index] == supo3[index]:
            count[3] += 1
    
    max_count = max(count.values())
    
    for key, value in count.items():
        if value == max_count:
            result.append(key)
    return result
