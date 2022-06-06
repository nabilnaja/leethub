class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time complexity: O(n log k) 
        Space complexity:  O(k)        
        """
        distances = {(x,y) : math.sqrt(x**2 + y**2) for x,y in points}
        points = [(x,y) for x,y in points]
        nsmallest = heapq.nsmallest(k, points, key = distances.get)
        return [[x,y ]for x , y in nsmallest]
        