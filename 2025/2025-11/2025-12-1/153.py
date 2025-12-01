class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # edge case when we find the sorted array, return leftmost pointer element
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            elif nums[r] > nums[m]:
                r = m - 1

        return result
