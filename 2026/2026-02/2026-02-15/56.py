class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort() # sort in order first
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            last_end = result[-1][1]
            if last_end >= intervals[i][0]:
                #overlap
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        return result