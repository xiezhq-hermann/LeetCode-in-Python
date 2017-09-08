class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        table = [[] for _ in range(target + 1)]
        for i in range(1, target + 1):
            for number in candidates:
                if number >= i:
                    if number == i:
                        table[i].append([i])
                    break
                for L in table[i - number]:
                    if number >= L[-1]:
                        table[i].append(L + [number])
                    else:
                        break
        return table[target]
