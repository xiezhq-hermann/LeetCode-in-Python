class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def formating(diction):
            sorted_keys = sorted(diction.keys())
            res = ""
            for key in sorted_keys:
                res += str(key)
                if diction[key] > 1:
                    res += str(diction[key])
            return res

        def merge_dict(d1, d2):
            result = dict(d1)
            for k, v in d2.iteritems():
                if k in result:
                    result[k] = result[k] + v
                else:
                    result[k] = v
            return result

        def parsing(formula, n=1):
            if "(" not in formula:
                counting = dict()
                atom = ["", "0"]
                for digit in formula:
                    if digit.isupper():
                        if atom[0]:
                            if atom[0] in counting:
                                counting[atom[0]] += max(int(atom[1]), 1) * n
                            else:
                                counting[atom[0]] = max(int(atom[1]), 1) * n
                        atom = [digit, "0"]
                    elif digit.islower():
                        atom[0] += digit
                    else:
                        atom[1] += digit
                else:
                    if atom[0]:
                        if atom[0] in counting:
                            counting[atom[0]] += max(int(atom[1]), 1) * n
                        else:
                            counting[atom[0]] = max(int(atom[1]), 1) * n
                return counting
            else:
                stack = []
                length = len(formula)

                for i in range(length):
                    if formula[i] == "(":
                        stack.append(i)
                    elif formula[i] == ")":
                        if len(stack) == 1:
                            break
                        stack.pop()
                left = stack.pop()
                right = bound = i

                num = "0"
                while right < length - 1:
                    if formula[right + 1].isdigit():
                        num += formula[right + 1]
                        right += 1
                    else:
                        break
                num = max(int(num), 1)
                a = parsing(formula[:left], n)
                b = parsing(formula[left + 1:bound], num * n)
                c = parsing(formula[right + 1:], n)
                res = merge_dict(merge_dict(a, b), c)
                return res

        return formating(parsing(formula))
