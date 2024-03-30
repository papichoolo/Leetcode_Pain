#Challenge to do this in o(n)

def twosum(listy,target):
    summer={}
    for i,y in enumerate(listy):
        complement=target-y
        if complement in summer:
            return [summer[complement],i]
        summer[y]=i #storing the index of the other number of the complement basically, 
        #in case the complement exists
    return []


