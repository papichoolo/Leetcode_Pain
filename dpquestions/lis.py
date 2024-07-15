def lis(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)
#Instead of returning the first element of DP, return the largest element
#bottom up approach
print(lis([4 ,2 ,8, 1, 18 ,14]))