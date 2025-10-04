class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            j = target - nums[i]
            if (j in nums) and (nums.index(j) != i):
                return [i, nums.index(j)]
        return []