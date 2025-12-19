class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        min_heap = []
        heapq.heapify(min_heap)

        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
        