class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = {len(s): 1} # empty string has only 1 decoding
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            result = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    result += dfs(i + 2)
            dp[i] = result
            return result
        return dfs(0)
        