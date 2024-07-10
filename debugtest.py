'''
You are given an array 
 of length 
 and can perform the following operation on the array:

Select a subarray from array 
 having the same value of elements and decrease the value of all the elements in that subarray by any positive integer 
.
Find the minimum number of operations required to make all the elements of array 
 equal to zero.

Input format

The first line contains an integer 
 denoting the number of elements in the array.
The next line contains space-separated integers denoting the elements of array 
.
Output format

Print the minimum number of operations required to make all the elements of array 
 equal to zero.'''  #basicall no of non consecutive elements in array

n = 5
arr =[2 ,2 ,1, 3, 1]


count = 0
i = 0

while i < n:
    count += 1
    value = arr[i]
    while i < n and arr[i] == value:
        i += 1
#this is beautiful code!
print(count)

