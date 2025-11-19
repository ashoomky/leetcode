class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        unique_elements = set()
        res = 0
        for r in range(len(s)):
            while s[r] in unique_elements:
                unique_elements.remove(s[l])
                l+=1
            unique_elements.add(s[r])
            res = max(res, r - l + 1)
        return res