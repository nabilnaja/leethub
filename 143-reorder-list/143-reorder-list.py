# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        head_copy = head
        
        while (head):
            stack.append(head)
            head = head.next
            
        head = head_copy
        for i in range(len(stack) - 1, (len(stack) // 2) - 1, -1):
            tail = stack[i]
            temp = head.next
            head.next = tail
            tail.next = temp
            head = tail.next 
            
        tail.next = None
            

        return head_copy
        