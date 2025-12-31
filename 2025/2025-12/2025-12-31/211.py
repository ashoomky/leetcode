class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        def dfs(j, root):
            current = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in current.children.values():
                        # run dfs on next letter and potential matching word for each children of the current node.
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]
            return current.end_of_word
        return dfs(0, self.root)
            
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)