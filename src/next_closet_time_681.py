class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def convert(digit):
            return 600*digit[0] + 60*digit[1] + 10*digit[2] + digit[3]

        def valid(time):
            base = convert(time)
            if time[0]*10+time[1] <= 24 and time[2]*10+time[3] <= 59 and base <= 1440:
                return True

        digit_base = [int(time[i]) for i in [0,1,3,4]]
        base = convert(digit_base)

        digit_set = set(digit_base)
        digit = [[i,j,m,n] for i in digit_set for j in digit_set for m in digit_set for n in digit_set]
        module = 1440
        
        res = digit_base
        for time in digit:
            if valid(time):
                diff = (convert(time) - base)%1440
                if diff and diff < module:
                    module = diff
                    res = time
        return str(res[0])+str(res[1]) + ':' + str(res[2]) + str(res[3])
