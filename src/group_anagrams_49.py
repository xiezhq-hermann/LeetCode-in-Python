class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in anagram:
                anagram[count].append(i)
            else:
                anagram[count] = [i]
        return list(anagram.values())
