class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagram_group = {}
        print(sorted("hello"))

        for word in strs:
            if "".join(sorted(word)) not in anagram_group.keys():
                anagram_group["".join(sorted(word))] = [word]
            else:
                anagram_group["".join(sorted(word))].append(word)
               

        result = []
        for values in anagram_group.values():
            result.append(values)
        
        return result

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected output: [["eat", "tea", "ate"], ["tan