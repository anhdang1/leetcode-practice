class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else: #if target < nums[mid]
                r = mid - 1
        
        return l
                
            
                
                
                
        

            
            

