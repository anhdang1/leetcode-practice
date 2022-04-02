class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for i in nums:
            x = nums.count(i)
            if x == 1:
                return i
        
        res = 0
        for i in nums:
            res = i ^ res
        return res
        """
        stack = []
        for i in nums:
            if i in stack:
                stack.remove(i)
            else:
                stack.append(i)
        for a in stack:
            return a