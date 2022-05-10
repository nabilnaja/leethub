class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i, j = len(text1), len(text2)
        memo = [[0] * (j+1) for _ in range(i+1)]
        for end1 in range(i-1, -1,-1):
            for end2 in range(j-1, -1,-1):
                if text1[end1] == text2[end2]:
                    memo[end1][end2] = memo[end1 +1][end2 + 1] + 1
                else:
                    memo[end1][end2] = max(memo[end1 +1][end2] , memo[end1][end2 + 1])
        return memo[0][0]