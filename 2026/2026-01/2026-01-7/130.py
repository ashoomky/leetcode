class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == columns or board[r][c] != "O"):
                return
            board[r][c] = "#"
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][columns - 1] == "O":
                dfs(r, columns - 1)
        
        for c in range(columns):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
