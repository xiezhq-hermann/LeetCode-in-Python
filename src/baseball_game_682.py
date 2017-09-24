class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        token_stack = []
        for t in ops:
            if t not in ['D', 'C', '+']:
                token_stack.append(int(t))
            else:
                if t == 'D':
                    token_stack.append(token_stack[-1] * 2)
                elif t == 'C':
                    token_stack.pop()
                else:
                    token_stack.append(sum(token_stack[-2:]))
        return sum(token_stack)
