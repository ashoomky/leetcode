class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        part = []
        
        # i keeps track of current substring we're on
        # j keeps track of the letter we're on in the current substring
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    result.append(part[:])
                return
            
            if self.is_palindrome(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            dfs(j, i + 1)
            
        dfs(0, 0)
        return result
            
    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
        

        