def solution(s):
    # 1개부터 최대 s / 2개 까지 압축이 가능하다
    # 압축을 시킨 최소 길이를 찾아 리턴하자
    compression_length = float('inf')
    compression_units = [1, *range(2, len(s) // 2 + 1, 1)]
    
    for compression_unit in compression_units:
        compression_results = ''
        compression_log = ''
        pointer = 0
        
        while(pointer < len(s)):
            base = s[pointer:pointer+compression_unit]
            
            count = 1
            for index in range(pointer+compression_unit, len(s), compression_unit):
                if base == s[index:index+compression_unit] and len(compression_results) % compression_unit == 0:
                    count += 1
                    pointer = index+compression_unit
                else:
                    break
            
            if count == 1:
                compression_results += s[pointer]
                pointer += 1
            else:
                compression_results += base
                compression_log += str(count)
        
        #print("unit", compression_unit, compression_results)
        compression_length = min(compression_length, len(compression_results) + len(compression_log))
        
    return compression_length
