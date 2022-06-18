class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        chars_i = [None] * 128
        r = l = 0
        res = 0
        
        while r < len(s):
            ch = ord(s[r])
            i = chars_i[ch]
            if i != None and i >= l and i < r:
                l = i + 1
            res = max(res, r - l + 1)
            chars_i[ch] = r
            r += 1
        return res
            
        