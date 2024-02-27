class Solution:
    def longestCommonPrefix(self, arr, n):
        if not arr or n == 0:
            return "-1"

        # Initialize the result as the first string
        result = arr[0]
        
        # Iterate through each string starting from the second one
        for i in range(1, n):
            j = 0
            # Compare characters of the current string with the result string
            while j < len(result) and j < len(arr[i]) and result[j] == arr[i][j]:
                j += 1
            
            # Update the result to be the common prefix found so far
            result = result[:j]
            
            # If no common prefix is found, return "-1"
            if not result:
                return "-1"
        
        return result
