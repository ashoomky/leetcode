class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.total = sum(nums)
        self.half = self.total // 2
        if self.total % 2 != 0:
            return False
        
        memo = {} # stores either true or false at each index ?
        def dfs(i, current_sum):
            if current_sum == self.half:
                return True
            if i == len(nums) or current_sum > self.half:
                return False
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            take = dfs(i + 1, current_sum + nums[i])
            skip = dfs(i + 1, current_sum)
            
            memo[(i, current_sum)] = take or skip

            return memo[(i, current_sum)]

        return dfs(0, 0)

