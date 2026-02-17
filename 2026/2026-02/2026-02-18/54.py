class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        while top <= bottom and left <= right:
            # left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            # top to bottom (right column)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            # bottom row (right to left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            # traverse last column on left only if necessary
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result