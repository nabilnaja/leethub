class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = [0] * 26
        res = 0
        l = 0
        ord_a = ord('A')
        
        for r in range(len(s)):
            
            ch = ord(s[r]) - ord_a
            window_count[ch] += 1
            max_ch = max(window_count)
            window_size = r - l + 1
            if window_size - max_ch > k:
                window_count[ord(s[l])- ord_a] -= 1
                l += 1   
            else: 
                res = max(res, window_size)
        return res
                
                
        
        