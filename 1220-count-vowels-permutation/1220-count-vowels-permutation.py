class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e','o' ,'u'], 'o': ['i', 'u'], 'u': ['a']}
        mod = 1000000007;
        @cache
        def dp(c, i = 1):
            if i == n:
                return 1
            return sum([dp(allowed_c, i+1) for allowed_c in rules[c]])
            
        return sum([dp(c) for c in rules]) % mod
        
        
        