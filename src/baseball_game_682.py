class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        token_stack = []
        for t in ops:
            if t == 'D':
                token_stack.append(token_stack[-1] * 2)
            elif t == 'C':
                token_stack.pop()
            elif t == '+':
                token_stack.append(sum(token_stack[-2:]))
            else:
                token_stack.append(int(t))
        return sum(token_stack)
