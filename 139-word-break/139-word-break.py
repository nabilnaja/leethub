class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dp(i = 0):
            if i >= n:
                return True
            r = n - i
            result = False
            for word in wordDict:
                if len(word) <= r and word == s[i: i + len(word)]:
                    result = result or dp(i + len(word))
            return result
        return dp()
                    