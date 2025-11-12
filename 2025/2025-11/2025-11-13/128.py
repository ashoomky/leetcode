class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sequences = {}

        if not nums:
            return 0

        for n in nums:
            if n in sequences:
                continue
            elif n - 1 in sequences and n + 1 in sequences:
                current = sequences[n - sequences[n-1]] + sequences[n + sequences[n+1]] + 1
                # updating
                sequences[n + sequences[n+1]] = current
                sequences[n - sequences[n-1]] = current
                sequences[n] = current
            elif n + 1 in sequences:
                sequences[n] = sequences[n+1] + 1
                sequences[n + sequences[n+1]] = sequences[n]
            elif n - 1 in sequences:
                sequences[n] = sequences[n-1] + 1
                sequences[n - sequences[n-1]] = sequences[n]
            else:
                sequences[n] = 1
                
        return max(sequences.values())