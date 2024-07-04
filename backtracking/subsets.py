class Solution:
    def subsets(self, nums):
        res=[]
        subset=[]

        def helper(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            helper(i+1)
        helper(0)
        return res
    

bruh=Solution()
print(bruh.subsets([1,2,3]))