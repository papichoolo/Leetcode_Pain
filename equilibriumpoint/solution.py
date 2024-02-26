class Solution:
    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Calculating the total sum of the array
        total_sum = sum(A)
        
        # Initializing left sum as 0
        left_sum = 0
        
        # Iterating through the array
        for i in range(N):
            # Subtracting the current element from the total sum
            total_sum -= A[i]
            
            # If left sum is equal to the total sum after removing current element,
            # then current index is the equilibrium point
            if left_sum == total_sum:
                return i + 1  # Return 1-based indexing
            
            # Updating left sum by adding the current element
            left_sum += A[i]
        
        # If no equilibrium point found, return -1
        return -1

# Example usage:
solution_obj = Solution()
A = [1, 3, 5, 2, 2]
N = len(A)
print(solution_obj.equilibriumPoint(A, N))  # Output: 3
