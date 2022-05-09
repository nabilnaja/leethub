class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Sub problems : s(i) minimum cost  from stair i, i-1 .. utill 0 (prefix)
        Original problem : r(n)
        Relate : r(i) = min (r(i - 1), r(i - 2)) + cost[i]
        Base :  r(0) =  
        Topological order : n , n-1, ..., 0
        Time : O(n) * O(1)
        """
        n = len(cost)
        @cache
        def dp(i = n):
            if i <= 1:
                return 0
            oneStepI, twoStepI = i - 1, i - 2
            oneStep = cost[i - 1] + dp(i - 1)
            twoStep = cost[i - 2] + dp(i - 2)

            return min(oneStep, twoStep)
        
        def dp():
            memo = [None for _ in range(n + 1)]
            memo[0], memo[1] = 0 , 0
            for i in range(2, n + 1):
                oneStepI, twoStepI = i - 1, i - 2
                oneStep = cost[oneStepI] + memo[oneStepI]
                twoStep = cost[twoStepI] + memo[twoStepI]
                memo[i] = min(oneStep, twoStep)
                
            return memo[i]
    
        def dp():
            memo = [None for _ in range(n + 1)]
            prev, prevSec = 0 , 0
            for i in range(2, n + 1):
                oneStep = cost[i - 1] + prev
                twoStep = cost[i - 2] + prevSec
                prev, prevSec = min(oneStep, twoStep), prev
                
            return prev
        return dp()