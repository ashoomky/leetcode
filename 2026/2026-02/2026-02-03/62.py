class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        rows, columns = len(grid), len(grid[0])
        memo = {} # store number of valid paths from current location

        # i = row, j = column
        def dfs(i, j):
            if i >= rows or j >= columns or i < 0 or j < 0:
                return 0
            if i == rows-1 and j == columns-1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1) # down, right
            
            return memo[(i, j)]
        return dfs(0, 0)

