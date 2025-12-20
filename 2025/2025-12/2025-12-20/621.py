class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # could use count = Counter(tasks) - pythons built in hashmap
        frequency_dict = {}
        for i in tasks:
            if i not in frequency_dict:
                frequency_dict[i] = 1
            else:
                frequency_dict[i] += 1

        max_heap = [-count for count in frequency_dict.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # pairs of [count, idletime]
        while max_heap or queue:
            time += 1
            if max_heap:
                # add 1 because we're using negative values, actually decrementing it
                count = 1 + heapq.heappop(max_heap)
                # now checking if there is still tasks left 
                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
   