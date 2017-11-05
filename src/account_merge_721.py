class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        if not accounts:
            return []

        def recur(accounts):
            email_dict, merged = {}, []
            count = 0
            for account in accounts:
                index_count = count
                flag = True

                for email in account[1:]:
                    if email in email_dict:
                        index_count = email_dict[email][1]
                        flag = False
                        break

                for email in account[1:]:
                    email_dict[email] = [account[0], index_count]

                if flag:
                    merged.append([account[0]] + sorted(list(set(account[1:]))))
                    count += 1
                else:
                    merged[index_count] = [account[0]] + \
                        sorted(
                            list(set(merged[index_count][1:]) | set(account[1:])))

            return merged

        res = recur(accounts)
        new = recur(res)
        while res != new:
            res = new
            new = recur(res)

        return res
