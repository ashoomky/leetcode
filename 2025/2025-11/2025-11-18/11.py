class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                max_area = max(max_area, area)
                l += 1
            elif height[r] <= height[l]:
                area = height[r] * (r - l)
                max_area = max(max_area, area)
                r -= 1
        
        return max_area