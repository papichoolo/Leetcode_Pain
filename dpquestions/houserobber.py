def houseroober(n):
    one, two= 0,0
    for i in n:
        temp= max(i+one,two)
        one= two
        two= temp
    return two