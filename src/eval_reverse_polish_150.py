class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        token_stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                token_stack.append(int(t))
            else:
                r, l = token_stack.pop(), token_stack.pop()
                if t == "+":
                    token_stack.append(l + r)
                elif t == "-":
                    token_stack.append(l - r)
                elif t == "*":
                    token_stack.append(l * r)
                else:
                    if l * r < 0 and l % r != 0:
                        token_stack.append(l / r + 1)
                    else:
                        token_stack.append(l / r)
        return token_stack.pop()
