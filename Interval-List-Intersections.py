class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if firstList == [] or secondList == []:
            return []
        
        p1 = p2 = 0

        output = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start1 > end2:
                p2 += 1
            elif start2 > end1:
                p1 += 1
            else :
                output.append([max(start1,start2), min(end1,end2)])
                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
        
        return output