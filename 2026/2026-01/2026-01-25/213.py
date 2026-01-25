class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        first = {}
        second = {}
        if n == 1:
            return nums[0]

        def dp(i, j, result):
            if i >= j:
                return 0
            if i in result:
                return result[i]
            result[i] = max(nums[i] + dp(i+2, j, result), dp(i + 1, j, result))
            return result[i]
        
        return max(dp(0, n-1, first), dp(1, n, second))
        