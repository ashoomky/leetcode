class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtrack([], nums, [False] * len(nums))
        return self.result

    def backtrack(self, perms, nums, pick):
        if len(nums) == len(perms):
            self.result.append(perms[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perms.append(nums[i])
                pick[i] = True
                self.backtrack(perms, nums, pick)
                perms.pop()
                pick[i] = False
               

        