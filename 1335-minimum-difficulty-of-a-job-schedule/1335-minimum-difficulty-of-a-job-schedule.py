class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Sub problems : dp(i, day) min difficulty starting from job i , i+1 untill n
        and starting from day day , day + 1 untill d
        Original problem : dp(0, 1)
        Relate : dp(i) = min(hardest + dp(j + 1, day + 1)) for all i <= j < n - (d - day) 
                        hardest = max(jobDifficulty[k]) for all i <= k <= j.
        Base :  
        Topological order : 0 , 1, ..., n ; 1, ..., d
        Time : 
        """
        n = len(jobDifficulty)
        
        if n < d:
            return -1
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
            
        @cache
        def dp(i = 0, day = 1):
            if day == d:
                return hardest_job_remaining[i]
            best = float("inf")
            hardest = 0
            for j in range(i, n - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1))
            return best
        #return dp()
        def dp():
            memo = [[float("inf")] * (d+1) for _ in range(n)]
            
            for i in range(len(memo)):
                memo[i][d] = hardest_job_remaining[i]
           
            for day in range(d - 1, 0, -1):
                for i in range(day - 1, n - (d - day)):
                    hardest = 0
                    for j in range(i, n - (d - day)):
                        hardest = max(hardest, jobDifficulty[j])
                        memo[i][day] = min(memo[i][day], hardest + memo[j + 1][day + 1])
            return memo[0][1]
                
        return dp()
            
        