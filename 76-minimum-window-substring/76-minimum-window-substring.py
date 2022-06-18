class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        
        if len(s) < len(t):
            return ''

        s_count, t_count = [0] * 128, [0] * 128
        ord_a = ord('A')

        criteria = 0
        valid_criteria = 0
        
        res = [0, float('inf')]

        for i in range(len(t)):
            ch_t = ord(t[i]) - ord_a
            if not t_count[ch_t]:
                criteria += 1
            t_count[ch_t] += 1

        l = 0
        for r in range(len(s)):
            ch_r = ord(s[r]) - ord_a
            s_count[ch_r] += 1
            if t_count[ch_r] and s_count[ch_r] == t_count[ch_r]:
                valid_criteria += 1

            while valid_criteria == criteria:
                res = res if r - l >= res[1] - res[0] else [l, r]

                ch_l = ord(s[l]) - ord_a

                s_count[ch_l] -= 1
                if t_count[ch_l] and s_count[ch_l] == t_count[ch_l] - 1:
                    valid_criteria -= 1
                l += 1

        return s[res[0]: res[1] + 1] if res[1] != float('inf') else ''