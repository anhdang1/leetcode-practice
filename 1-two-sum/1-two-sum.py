class Solution:
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if target - nums[i] == nums[k]:
                    return [i,k]
                
                
        """
        prevMap = {}  #val: index
        
        for i, n in enumerate(nums):  #i is index and n is value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i   #for n value the index is i
        """
            
        