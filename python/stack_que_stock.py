## Question
# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

## My solution
def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[j] < prices[i]:
                answer.append(j-i)
                break
        else:
            answer.append(len(prices)-i-1)
    return answer
 
## Good solution
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
