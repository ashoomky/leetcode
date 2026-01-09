class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        hashmap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        
        output = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
            
            