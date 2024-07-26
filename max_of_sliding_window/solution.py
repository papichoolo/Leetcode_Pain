from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []  # To store the maximum of each sliding window
        q = deque()  # To store the indices of useful elements within the window
        l = r = 0  # Initialize left and right pointers of the sliding window

        while r < len(nums):  # Iterate over the list with the right pointer
            # Remove elements from the deque from the right if they are smaller than the current element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)  # Append the current element index to the deque

            # Remove elements from the deque from the left if they are out of the current window
            if l > q[0]:
                q.popleft()

            # Once the window size reaches 'k', append the maximum element (at the front of the deque) to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])  # The element at the front of the deque is the maximum in the current window
                l += 1  # Slide the window by incrementing the left pointer
            r += 1  # Move the right pointer to expand the window

        return output  # Return the list of maximums for each sliding window
