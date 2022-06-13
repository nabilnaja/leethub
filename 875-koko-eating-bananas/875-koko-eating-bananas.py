class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Time complexity: O(log n * m)  
        Space complexity:  O(1)        
        """
        l, r = 1, max(piles)
        def can_eat(eat_capacity):
            hours_to_eat = 0
            for num in piles:
                hours_to_eat += math.ceil(num / eat_capacity)
            return h >= hours_to_eat  
            
        while l <= r:
            mid = l + (r - l) // 2
            if can_eat(mid):
                r = mid - 1   
            else:
                l = mid + 1
        return l
                
        