class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        
        count = { i: Counter(item) for i, item in enumerate(strs)}
        print(count)
        @cache
        def dp(i = 0, m_rest = m, n_rest = n):
            if m_rest < 0 or n_rest < 0:
                return float("-inf")
            
            if i == l:
                return 0
            
            return max(dp(i+1, m_rest,n_rest ), dp(i+1, m_rest - count[i]['0'], n_rest - count[i]['1']) + 1)
            

        return dp()
            
            
            
            
            
        
             
            