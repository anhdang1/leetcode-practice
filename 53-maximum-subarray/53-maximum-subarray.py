class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0
        
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum
        
                    
                    
                    