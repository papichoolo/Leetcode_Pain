def partial_selection_sort(A, B, n):
    indices = sorted(range(n), key=lambda i: A[i])
    
    sorted_B = [B[i] for i in indices]
    return sorted_B
# Example usage:
array_A = [32,4,53,2,0,18]
array_B = [21,11,9,3,16,36]
n_iterations = 3

sorted_array_B = partial_selection_sort(array_A, array_B, n_iterations)
print(sorted_array_B)
