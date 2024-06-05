class Solution:
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


    
    def helper(self, nums):
        rob1, rob2= 0,0 
        for n in nums:
            bruh= max(n+rob1,rob2)
            rob1=rob2
            rob2=bruh
        return rob2
    
# Time complexity: O(n) 
bruh= Solution()
print(bruh.rob([2,3,2]))