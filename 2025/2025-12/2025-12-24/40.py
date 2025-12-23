class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def dfs(i, combination, total):
            if total == target:
                result.append(combination[:])
                return
            if  i == len(candidates) or total > target:
                return

            # include current number
            combination.append(candidates[i])
            dfs(i + 1, combination, total + candidates[i])
            combination.pop() # pop to backtrack

            # skip current number
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, combination, total)
        
        dfs(0, [], 0)
        return result