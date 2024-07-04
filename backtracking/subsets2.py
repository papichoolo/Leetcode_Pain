class Solution:
    def subsets2(self,nums):
        nums.sort()
        res=[]

        subset=[]

        def helper(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            #add the element to the subset

            subset.append(nums[i])
            helper(i+1)

            subset.pop()
            #skipping the element and its duplicates

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1)
        helper(0)

        return res
    
bruh=Solution()
print(bruh.subsets2([1,2,2]))
             