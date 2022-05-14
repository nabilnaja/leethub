class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def is_valid_iter(s):
            return True if 10 <= int(s) <= 26 else False
        one_ahead = 1 if s[n-1] != '0' else 0
        two_ahead = 1 
            
        for i in range(n - 2, -1, -1):
            current = 0
            if s[i] != '0':
                current = two_ahead + one_ahead if is_valid_iter(s[i : i + 2]) else one_ahead
            one_ahead, two_ahead = current , one_ahead
            
        return one_ahead
            
        