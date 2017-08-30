class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            common = strs[0]
            for i in strs:
                for j in range(len(common), -1, -1):
                    if i[:j] == common[:j]:
                        break
                common = common[:j]
            return common
