class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time complexity: O(nlogn) 
        Space complexity:  O(n)         
        """
        negative_stones = [-x for x in stones]
        heapq.heapify(negative_stones)
        while len(negative_stones) > 1:
            first, second = heapq.heappop(negative_stones), heapq.heappop(negative_stones)
            if first != second:
                new_weight = first - second if first < second else second - first
                heapq.heappush(negative_stones, new_weight)
            
        return -negative_stones[0] if negative_stones else 0
        