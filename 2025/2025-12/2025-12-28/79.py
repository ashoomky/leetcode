class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # conditions to check if the index and results are still valid
            if (min(r, c) < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in seen):
                return False
            
            seen.add((r, c))
            # up, down, right, left
            result = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            seen.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False



        