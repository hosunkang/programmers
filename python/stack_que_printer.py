## Question
# priorities	        location	return
# [2, 1, 3, 2]	      2	        1
# [1, 1, 9, 1, 1, 1]	0	        5

## My solution
import numpy as np

def solution(priorities, location):
    answer = 0
    while 1:
        max = np.argmax(priorities)
        left_max = priorities[:max]
        right_max = priorities[max:]
        if max == location:
            return answer+1
        elif max > location:
            location += len(right_max)
        else:
            location -= len(left_max)
        priorities = priorities[max:] + left_max
        del priorities[0]
        location -= 1
        answer += 1
        
## Good solution
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
