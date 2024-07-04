#here we always import heapq, cuz i dont want to make things unnecessarily complicated

import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.minheap, self.k= nums, k
        heapq.heapify(self.minheap)

        while len(self.minheap)>k:
            heapq.heappop(self.minheap)
        
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        heapq.heappush(self.minheap,val)
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        """
        :type val: int
        :rtype: int
        """
        
#So this is a solution based on heaps, specifically min heaps of size(K), we set the nums as the heap.
#in add(), we push the element to the heap, and to make sure the size of the minheap stays three, and then we return the root node of the minheap to return the third largest element all the time.