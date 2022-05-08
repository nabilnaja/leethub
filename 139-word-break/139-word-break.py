class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dp(i = 0):
            if i == n:
                return True
            for end in range(i + 1, len(s) + 1):
                if s[i:end] in wordDict and dp(end):
                    return True
            return False
        return dp()
                    