class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity:  O(n)
        """
        visited_letters = {}
        j = 0
        i = 0
        res = 0
        while j < len(s):
            if s[j] in visited_letters:
                res = max(res, j - i)
                i = j = visited_letters[s[j]] + 1
                visited_letters = {}
            else:
                visited_letters[s[j]] = j
                j += 1
        else: 
            res = max(res, j - i)
        return res
            
        