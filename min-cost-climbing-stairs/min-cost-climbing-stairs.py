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
        prev, prevSec = 0 , 0
        for i in range(2, n + 1):
            oneStep = cost[i - 1] + prev
            twoStep = cost[i - 2] + prevSec
            prev, prevSec = min(oneStep, twoStep), prev
                
        return prev