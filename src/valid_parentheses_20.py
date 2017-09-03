class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        par_dic = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif i in (')', ']', '}'):
                if stack == [] or par_dic[stack.pop()] != i:
                    return False
            else:
                return False
        return stack == []
