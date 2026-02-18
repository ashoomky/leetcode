class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, columns = len(matrix), len(matrix[0])
        marked_rows = set()
        marked_cols = set()
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    marked_rows.add(i)
                    marked_cols.add(j)
        
        for i in range(rows):
            for j in range(columns):
                if i in marked_rows:
                    matrix[i][j] = 0
                if j in marked_cols:
                    matrix[i][j] = 0
        