class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Time complexity: O(n log n) 
        Space complexity:  O(n)         
        """
        pair = sorted([(p, (target - p)/s) for p,s in zip(position, speed)])
        stack = []
        for item in pair:
            while stack and stack[-1] <= item[1]:
                stack.pop()
            stack.append(item[1])
        return len(stack) 
        