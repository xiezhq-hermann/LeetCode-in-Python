class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.set = set(dict)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        chars = [chr(i + 97) for i in range(26)]
        for i, char in enumerate(word):
            for j in chars:
                if j != char and (word[:i] + j + word[i + 1:]) in self.set:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
