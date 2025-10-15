class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result = []

        for i in letters:
            if i > target:
                result.append(i)
        
        if result:
            return min(result)
        else:
            return letters[0]