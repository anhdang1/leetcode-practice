class Solution:
    def longestCommonPrefix(self, strs):
        
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += s[i]
        
        return res
        