class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sol, s=[], leftSum=0, rightSum=0):
            if len(s) == n * 2:
                sol.append(''.join(s))
                return
            if leftSum > rightSum:
                s.append(')')
                backtrack(sol, s, leftSum, rightSum + 1)
                s.pop()
            if leftSum < n:
                s.append('(')
                backtrack(sol, s, leftSum + 1, rightSum)
                s.pop()

        result = []
        backtrack(result)
        return result