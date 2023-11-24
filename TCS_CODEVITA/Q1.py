def selection_sort(A, B, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j

        # Swap elements in array A
        A[i], A[min_index] = A[min_index], A[i]

        # Reflect swaps in array B
        B[i], B[min_index] = B[min_index], B[i]

    return B

# Input
A = list(map(int, input().split()))
B = list(map(int, input().split()))
n = int(input())

# Perform selection sort and print the modified array B
result = selection_sort(A, B, n)
print(" ".join(map(str, result)))
