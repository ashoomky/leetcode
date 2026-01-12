class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)   
        adj = {i: [] for i in range(n)}
        # comparing the point with every other point in the graph
        for i in range(n):
            x1, x2 = points[i]
            for j in range(i + 1, n):
                y1, y2 = points[j]
                distance = abs(x1 - y1) + abs(x2 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        result = 0
        visit = set()
        min_heap = [[0, 0]] # cost, point
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            result += cost
            visit.add(i)
            for cost, neighbour in adj[i]:
                if neighbour not in visit:
                    heapq.heappush(min_heap, [cost, neighbour])

        return result

        