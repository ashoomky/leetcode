class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
  
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
       
        while stones:
      
            if len(stones) == 1:
                return -stones[0]

            x = -stones[1]
            y = -stones[0]
            if x == y:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                old_y = heapq.heappop(stones)
                # destroy x
                x = heapq.heappop(stones)
                heapq.heappush(stones, -((-old_y) - (-x))) 
        return 0

