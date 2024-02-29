class Solution:
    def trappingWater(self, arr, n):
        if n <= 2:  # No water can be trapped if there are less than 3 blocks
            return 0
        
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
        
        # Fill right_max array
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        water_trapped = 0
        # Calculate trapped water for each block
        for i in range(1, n - 1):
            water_trapped += max(0, min(left_max[i], right_max[i]) - arr[i])
        
        return water_trapped