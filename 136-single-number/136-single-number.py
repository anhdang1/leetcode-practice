class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            x = nums.count(i)
            if x == 1:
                return i