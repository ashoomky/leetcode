class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, columns = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, previous_height):
            if ((r, c) in visit or r < 0 or c < 0 
            or r == rows or c == columns 
            or heights[r][c] < previous_height):
                return
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        
        for c in range(columns):
            # loop for pacific ocean top
            dfs(0, c, pacific, heights[0][c])
            # loop for atlantic ocean bottom
            dfs(rows - 1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            # loop for pacific ocean left
            dfs(r, 0, pacific, heights[r][0])
            # loop for atlantic ocean right
            dfs(r, columns - 1, atlantic, heights[r][columns-1])
        
        result = []
        for r in range(rows):
            for c in range(columns):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result


        