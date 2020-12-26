def solution(bridge_length, weight, truck_weights):
    if bridge_length == 1:
        return len(truck_weights)
    
    time = 0
    stack = []
    truck_weight = truck_weights.pop(0)
    stack.append((truck_weight, time))
    stored_weight = truck_weight
    
    while(stack):
        time += 1
        if time - stack[0][1] == bridge_length:
            stored_weight -= stack.pop(0)[0]
        if truck_weights:
            if stored_weight + truck_weights[0] <= weight:
                truck_weight = truck_weights.pop(0)
                stack.append((truck_weight, time))
                stored_weight += truck_weight
    return time + 1
