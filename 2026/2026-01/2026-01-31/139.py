class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
             
        return dfs(0)
            
