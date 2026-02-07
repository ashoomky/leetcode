class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {} #  key: (index, current sum) value: ways its valid

        def dfs(i, current):
            if i == len(nums) and current == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, current) in memo:
                return memo[(i, current)]
            add = dfs(i + 1, current + nums[i]) 
            subtract = dfs(i + 1, current - nums[i])
            memo[(i, current)] = add + subtract
            return memo[(i, current)]

                
        return dfs(0, 0)
            