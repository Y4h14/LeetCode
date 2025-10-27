class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        week = 0
        for i in range(n):
            if i % 7 == 0:
                week += 1
            sum += week + (i % 7)
        return sum