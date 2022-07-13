# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time complexity: O(n log k)  
        Space complexity:  O(k)        
        """
        k = len(lists)
        index = [ (1,i) for i in range(k)]
        heap = [(lists[i].val, i, lists[i]) for i in range(k) if lists[i]]
        if not heap:
            return None
        heapq.heapify(heap)
        res_head = ListNode()
        res_tail = res_head
        while heap:
            lower = heapq.heappop(heap)
            res_tail.next = ListNode(lower[0])
            res_tail = res_tail.next
            if(lower[2].next):
                k += 1
                heapq.heappush(heap, (lower[2].next.val, k , lower[2].next))
        return res_head.next