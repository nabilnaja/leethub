class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        window_count = [0] * 26
        res = 0
        max_f = 0
        l = 0
        ord_a = ord('A')
        
        for r in range(len(s)):
            
            ch = ord(s[r]) - ord_a
            window_count[ch] += 1
            max_f = max(window_count[ch], max_f)
            window_size = r - l + 1
            if window_size - max_f > k:
                window_count[ord(s[l])- ord_a] -= 1
                l += 1   
            else: 
                res = max(res, window_size)
        return res
                
                
        
        