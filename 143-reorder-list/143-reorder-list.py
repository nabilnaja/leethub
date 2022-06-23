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
       
        slow_pointer = fast_pointer = head
            
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        
        prev, curr = None, slow_pointer
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        list1, list2 = head, prev
        
        while list2.next:
            list1.next, list1 = list2, list1.next
            list2.next, list2 = list1, list2.next

        return head 
        
        
            