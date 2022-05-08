class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dp(i = 0):
            if i == n:
                return True
            r = n - i
            for word in wordDict:
                if len(word) <= r and word == s[i: i + len(word)] and  dp(i + len(word)):
                    return True
            return False
        return dp()
                    