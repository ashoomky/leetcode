class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_length, result = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)] # array to check if it is a palindrome
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if result_length < (j - i + 1):
                        result = i
                        result_length = j - i + 1
        
        return s[result:result_length + result]