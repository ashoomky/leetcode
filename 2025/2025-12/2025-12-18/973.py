class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        max_heap = []
        heapq.heapify(max_heap)

        for i in range(len(points)):
            distance = math.sqrt((points[i][0]*points[i][0]) + (points[i][1] * points[i][1]))
            heapq.heappush(max_heap, [-distance, points[i]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        for j in range(len(max_heap)):
            result.append(max_heap[j][1])
        return result
