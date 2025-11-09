class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1

        return False

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)

# O(2n) solution
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """

#         dic = {}

#         for i in range(len(nums)):
#             if nums[i] in dic:
#                 dic[nums[i]] += 1
#             else:
#                 dic[nums[i]] = 1
        
#         for k, v in dic.items():
#             if v >= 2:
#                 return True

#         return False
        