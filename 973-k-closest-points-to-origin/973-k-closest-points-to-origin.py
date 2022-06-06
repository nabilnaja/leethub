class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time complexity: O(n log k) 
        Space complexity:  O(k)        
        """
        heap = [(math.sqrt(i[0]**2 + i[1]**2), i) for i in points]
        nsmallest = heapq.nsmallest(k, heap)
        return [i[1] for i in nsmallest]
        