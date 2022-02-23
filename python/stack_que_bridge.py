## Question
# bridge_length	weight	truck_weights	                  return
# 2	            10	    [7,4,5,6]	                      8
# 100	          100	    [10]	                          101
# 100	          100	    [10,10,10,10,10,10,10,10,10,10]	110

## My solution
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = []
    location = []
    while len(truck_weights) != 0 or len(on_bridge) !=0:
        print(truck_weights)
        if len(on_bridge) == 0:
            on_bridge.append(truck_weights.pop(0))
            location.append(1)
        else:
            location = list(map(lambda x:x+1, location))
            if location[0] > bridge_length:
                del on_bridge[0]
                del location[0]
            if len(truck_weights) != 0 and sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
                location.append(1)
        answer+=1
        print(on_bridge, location, answer)
    return answer

## Good solution
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    print(bridge)
    total_weight = 0
    step = 0
    truck_weights.reverse()
    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1
    step += bridge_length
    return step
