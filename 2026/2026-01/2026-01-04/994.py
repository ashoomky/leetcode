class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, columns = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
      
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) 
                    and new_col in range(columns) 
                    and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        return -1
                        
            
                
            

        