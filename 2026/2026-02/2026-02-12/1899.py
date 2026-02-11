class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        foundA = False
        foundB = False
        foundC = False
        for i in range(len(triplets)):
            current = triplets[i]
            if current[0] > target[0] or current[1]> target[1] or current[2] > target[2]:
                continue
            if current[0] == target[0]:
                foundA = True
            if current[1] == target[1]:
                foundB = True
            if current[2] == target[2]:
                foundC = True
            
        return foundA and foundB and foundC
            