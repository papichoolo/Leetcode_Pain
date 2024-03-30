class Solution:
    # Function to partition the array around the range such 
    # that the array is divided into three parts.
    def threeWayPartition(self, array, a, b):
        n = len(array)
        
        # Initialize low and high pointers for the three-way partitioning
        low = 0
        mid = 0
        high = n - 1
        
        # Perform Dutch National Flag algorithm
        while mid <= high:
            if array[mid] < a:
                # Swap array[low] and array[mid]
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
            elif array[mid] > b:
                # Swap array[mid] and array[high]
                array[mid], array[high] = array[high], array[mid]
                high -= 1
            else:
                mid += 1
        
        # Return 1 to indicate successful partitioning
        return 1
"""So Basically like in DNF if arr[mid]=0, then swap mid and low, mid and low increases by one. if arr[mid]=1, mid increases. if arr[mid]=2 then swap mid and high and decrease high pointer."""
#so ddo that but with the range of a and b
# Example usage
sol = Solution()
array = [1, 2, 3, 3, 4]
a, b = 1, 2
result = sol.threeWayPartition(array, a, b)
if result == 1:
    print("Modified array:", array)
