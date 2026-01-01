# dfs solution
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # up, down, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, columns = len(grid), len(grid[0])
        def dfs(row, col):
            if row >= rows or row < 0 or col >= columns or col < 0 or grid[row][col] == "0":
                return 
            
            # making current island 0 to sink it so we don't go back
            grid[row][col] = "0"
            # exploring the four cells around our current one to see if it is still part of the group
            for direction_row, direction_col in directions:
                dfs(row + direction_row, col + direction_col)

        # running dfs only on the 1 we've encountered - the rest of the search will be carried out above
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1                
        
        return islands

# bfs solution
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        rows, columns = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] == "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for direction_row, direction_col in directions:
                    new_row, new_col = direction_row + row, direction_col + col
                    if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= columns or grid[new_row][new_col] == "0":
                        continue
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = "0"

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
        
        