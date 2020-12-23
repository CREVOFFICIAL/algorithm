def solution(dartResult):
    numbers = []
    commands = []
    darts = list(dartResult)
    
    bonus = {"S": 1, "D": 2, "T": 3}
    options = {"*": 2, "#": -1}
    
    isFirst = True
    isLastDigit = False
    numberString = ""
    commandString = ""
    
    for dart in darts:
        if dart.isdigit():
            numberString += dart
            if not isFirst and not isLastDigit:
                commands.append(commandString)
                commandString = ""
            else:
                isFirst = False
            isLastDigit = True
        elif isLastDigit and dart.isalpha():
            isLastDigit = False
            numbers.append(int(numberString))
            numberString = ""
            commandString += dart
        else:
            commandString += dart
    
    
    if numberString != "":
        numbers.append(int(numberString))
    
    if commandString != "":
        commands.append(commandString)
        
    
    for index, command in enumerate(commands):
        for dart in command:
            if dart in bonus:
                numbers[index] = pow(numbers[index], bonus[dart])
            elif dart in options:
                if dart == "*":
                    if index > 0:
                        numbers[index - 1] = numbers[index - 1] * 2
                    numbers[index] = numbers[index] * 2
                else:
                    numbers[index] = numbers[index] * -1
    
    answer = sum(numbers)
    return answer
