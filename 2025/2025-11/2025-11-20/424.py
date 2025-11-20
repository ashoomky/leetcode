class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # checking for if the amount of elements we can replace is greater than the given number 
            while (r - l + 1) - max(count.values()) > k:
                # shrinking the window from the left
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
            
            
        

        