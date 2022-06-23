# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        else:
            slow.next = slow.next.next
        return dummy.next
            
        