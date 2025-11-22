class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        frequency_s1 = [0] * 26
        frequency_s2 = [0] * 26
        for i in range(len(s1)):
            frequency_s1[ord(s1[i]) - ord('a')] += 1
            frequency_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if frequency_s1[i] == frequency_s2[i]:
                matches += 1
          
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            frequency_s2[index] += 1
            if frequency_s2[index] == frequency_s1[index]:
                matches += 1
            elif frequency_s2[index] == frequency_s1[index] + 1:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            frequency_s2[index] -= 1
            if frequency_s2[index] == frequency_s1[index]:
                matches += 1
            elif frequency_s2[index] == frequency_s1[index] - 1:
                matches -= 1
            l += 1
        return matches == 26