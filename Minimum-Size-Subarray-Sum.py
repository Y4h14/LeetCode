class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        back = 0
        l = len(nums)+1
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= target:
                l = min(l, i - back + 1)
                sum -= nums[back]
                back +=1
        return l if l != len(nums)+1 else 0
            
            
            