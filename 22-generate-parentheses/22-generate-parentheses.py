class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time complexity: O(4^^n / (n * n **1/2)) 
        Space complexity:  O(4^^n / (n * n **1/2))         
        """
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