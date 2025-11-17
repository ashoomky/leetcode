class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            # checking that we are not on the same element (don't want to do operation on same element again) 
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]]) 
                    l += 1
                    # while loop so we don't have the same number again to avoid duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return result