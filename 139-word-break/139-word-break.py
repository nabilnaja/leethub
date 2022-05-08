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
        #return dp()
        def dp():
            memo = [False] * ( n + 1)
            memo[0] =  True
            for i in range(1, len(memo)):
                for j in range(i):
                    if memo[j] and s[j:i] in wordDict:
                        memo[i] = True
                        break
            return memo[n]
        return dp()