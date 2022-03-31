class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxProf = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProf = max(maxProf, profit)
            else:
                l = r
            r += 1
            
        return maxProf
        
        """
        maxProf = 0
        diff = 0
        for i in range(len(prices)):
            for k in range(i+1, len(prices)):
                diff = prices[k] - prices[i]
                
                maxProf = max(maxProf, diff)
        return maxProf """
                       