class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges = defaultdict(list)

        for u, v, w in times:
            #(end node, time it takes)
            edges[u].append((v, w))
        
        # distance from source node to all nodes (weighted edge, node)
        minheap = [(0, k)]
        visit = set()
        time = 0

        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, weight)

            for neighbour, w in edges[node]:
                if neighbour not in visit:
                    heapq.heappush(minheap, (weight + w, neighbour))
        
        if len(visit) == n:
            return time
        else:
            return -1
                