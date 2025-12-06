class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # finding pivot point
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary_search(left, right):
            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    right = m - 1
                else:
                    left = m + 1
            return -1
        
        # running search on first half of the list first
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        # running search on second half if not in first half
        return binary_search(pivot, len(nums)-1)
        