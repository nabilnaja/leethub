class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        chars = [None] * 128
        
        r = l = 0
        res = 0
        
        while r < len(s):
            
            ch = s[r]
            index = chars[ord(ch)]
            if index != None and index >= l and index < r:
                l = index + 1
            res = max(res, r - l + 1)
            chars[ord(ch)] = r
            r += 1
        return res
            
        