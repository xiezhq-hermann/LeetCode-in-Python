class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateSub(left, right, sub, res = []):
            if left == 0:
                res.append(sub + ')' * right)
            else:
                if right > left:
                    generateSub(left, right - 1, sub + ')')
                generateSub(left - 1, right, sub + '(')
            return res
        return generateSub(n, n, '')
