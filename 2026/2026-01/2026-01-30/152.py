class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        current_min, current_max = 1, 1

        for n in nums:
            temp = current_max * n
            current_max = max(n * current_max, n * current_min, n)

            current_min = min(temp, n * current_min, n)
            result = max(result, current_max)
        return result

        
        # result = nums[0]

        # for i in range(len(nums)):
        #     current = nums[i]
        #     result = max(result, current)
        #     for j in range(i + 1, len(nums)):
        #         current *= nums[j]
        #         result = max(result, current)
        # return result
                
