class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        sorted_freq = sorted(freq.items(), key=lambda x:x[1])
        return [key[0] for key in sorted_freq[-k:]]
        