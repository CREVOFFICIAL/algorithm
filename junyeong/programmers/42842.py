def solution(brown, yellow):
    sum = yellow+brown
    for divisor in range(1, yellow+1):
        if yellow % divisor == 0:
            width = (yellow // divisor) + 2
            height = sum // width
            if width >= height and width * height == sum:
                return [width, height]
