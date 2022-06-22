# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Time complexity: O(n)  
        Space complexity:  O(n)        
        """
        if not head:
            return head 
        
        def reverseLinkedList(head):
            if not head or not head.next:
                return head
            tail = reverseLinkedList(head.next)
            head.next.next = head
            head.next = None
            return tail
        
       
        slow_pointer = fast_pointer = head
            
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
            
        list1, list2 = head, reverseLinkedList(slow_pointer) 

        while list2.next:
            list1.next, list1 = list2, list1.next
            list2.next, list2 = list1, list2.next
        
        return head 
        
        
            