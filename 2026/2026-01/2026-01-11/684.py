class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = [i for i in range(n + 1)] # parent of the ith node in position
        rank = [1] * (n + 1) #size of each connected component
        
        # find the parent of the given node
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
            
        
        def union(n1, n2):
            # seeing if the nodes share a parent. if they do, they're connected and return false.
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += p2
            else:
                parent[p1] = p2
                rank[p2] += p1
            return True


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        

