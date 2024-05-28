def jumpgame(n, arr):
    target=n-1
    res=0
    while target != 0:
        jumped= False
        for i in range(target):
            if arr[i]!=0 and i+arr[i]>=target:
                target=i
                res+=1
                break
            if arr[i]==0:
                continue
    return 1 if res!=0 else 0

#can manipulate the return statement if you are counting the number of jumps

#Greedy approach given below (only counts if it is possible or no)
def canReach(n, arr):
    max_reachable = arr[0]
    for i in range(1, n):
        if max_reachable < i:
            return 0
        max_reachable = max(max_reachable, i + arr[i])
    return 1