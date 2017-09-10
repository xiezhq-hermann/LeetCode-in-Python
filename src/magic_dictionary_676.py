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
        def checkOne(word, member):
            length = len(word)
            if len(member) != length:
                return False
            flag = False
            for i in range(length):
                if word[i] != member[i]:
                    if flag:
                        return False
                    flag = True
            return flag

        for member in self.set:
            if checkOne(word, member):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
