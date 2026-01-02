class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, columns = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        area = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))                  

        return area