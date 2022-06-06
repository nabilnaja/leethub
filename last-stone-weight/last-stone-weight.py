class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time complexity: O(nlogn) 
        Space complexity:  O(1)         
        """
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)
            
        return -stones[0] if stones else 0