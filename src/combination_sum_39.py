class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ref_set = set(candidates)
        table = [[] for _ in range(target + 1)]

        for i in range(1, target + 1):
            tag = 1
            flag = 1  # a flag for determine range
            while tag <= i // 2:
                if table[tag] and table[i - tag]:
                    if flag:
                        table[i] = [m + n for m in table[tag]
                                    for n in table[i - tag]]
                        flag = 0
                    elif tag in ref_set:
                        for combination in table[i - tag][::-1]:
                            if combination[0] >= tag:
                                table[i].append([tag] + combination)
                            else:
                                break
                tag += 1

            if i in ref_set:
                table[i].append([i])

        return table[target]
