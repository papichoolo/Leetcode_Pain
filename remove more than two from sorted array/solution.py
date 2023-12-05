class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i < len(nums)-2:
            if(nums[i]==nums[i+2]):
                del nums[i]
            else:
                i+=1

        
        return len(nums)