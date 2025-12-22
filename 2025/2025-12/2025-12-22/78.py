class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset[:])
                return

            # decision to add value to subset
            subset.append(nums[i])
            dfs(i + 1) # to run on the next element

            # decision to not add value to subset
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return result

        

        