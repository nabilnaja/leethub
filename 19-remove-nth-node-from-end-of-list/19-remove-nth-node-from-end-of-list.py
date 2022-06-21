# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        fast_pointer = dummy
        slow_pointer = dummy
        
        for i in range(n + 1):
            fast_pointer = fast_pointer.next
                
        while fast_pointer:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        else:
            slow_pointer.next = slow_pointer.next.next 
                
        return dummy.next