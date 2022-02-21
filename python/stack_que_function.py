## Question
# progresses	              speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

## My solution
def solution(progresses, speeds):
    answer = []
    while 1:
        count = 0
        progresses = [x+y for x,y in zip(progresses, speeds)]
        while len(progresses) != 0 and progresses[0] >= 100:
            count += 1
            del progresses[0]
            del speeds[0]
        if count > 0:
            answer.append(count)
        if len(progresses) == 0:
            break
    return answer
  
## Good solution
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
