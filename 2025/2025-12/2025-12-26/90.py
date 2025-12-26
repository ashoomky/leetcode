class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        def dfs(i, combination):
            if i == len(nums):
                result.append(combination[:])
                return
            
            combination.append(nums[i])
            dfs(i + 1, combination)
            combination.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, combination) 
        
        dfs(0, [])
        return result