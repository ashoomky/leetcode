class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # mapping the prereqs to each course
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if prereq_map[course] == []:
                return True
            
            seen.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            seen.remove(course)
            prereq_map[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        
           