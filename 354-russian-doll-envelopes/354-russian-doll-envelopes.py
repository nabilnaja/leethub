class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes_y = [i[1] for i in envelopes]
        dp = []
        for i in range(len(envelopes_y)):
            idx = bisect_left(dp, envelopes_y[i]) 
            if idx == len(dp):
                dp.append(envelopes_y[i])
            else:
                dp[idx] = envelopes_y[i]
        return len(dp)
