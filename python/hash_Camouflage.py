## Question
#clothes	                                                                                return
#[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
#[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	            3

## My solution
def solution(clothes):
    answer = 1
    clothes_count = {}
    for values in clothes:
        if values[1] in clothes_count:
            clothes_count[values[1]] += 1
        else:
            clothes_count[values[1]] = 2
    for value in clothes_count.values():
        answer *= value
    answer -= 1
    return answer
 
## Good solution
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
