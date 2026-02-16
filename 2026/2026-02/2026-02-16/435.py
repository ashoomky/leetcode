class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        result = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                result += 1
                previous_end = min(previous_end, end)

        return result
            


            
         
        