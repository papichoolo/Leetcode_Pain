class Solution(object):
    def arraySign(self, nums):
        prod = 1  # Initialize the product to 1
        for num in nums:
            if num == 0:
                return 0  # If any element is 0, the product will be 0
            if num < 0:
                prod *= -1  # If an element is negative, change the sign of the product
        return prod
