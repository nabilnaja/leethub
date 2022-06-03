class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Time complexity: O(n log n) 
        Space complexity:  O(n)         
        """
        pair = sorted([(p, (target - p) / s ) for p,s in zip(position, speed)], reverse = True)
    
        stack = []
        for p, t in pair:
            stack.append(t)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return(len(stack))