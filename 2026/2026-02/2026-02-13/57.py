class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []
        for start, end in intervals:
            if end < newInterval[0]:
                result.append([start, end])
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        result.append(newInterval)

        return result
