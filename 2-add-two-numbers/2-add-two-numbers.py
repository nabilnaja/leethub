# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1 , l2, over = 0):
            if not l1 and not l2:
                return ListNode(over) if over else None
            if not l1:
                sum = l2.val + over
                over = 0
                if sum > 9:
                    res = ListNode(sum - 10)
                    over = 1
                else:
                    res = ListNode(sum)   
                res.next = helper(None, l2.next, over)
                return res
            elif not l2:
                sum = l1.val + over
                over = 0
                if sum > 9:
                    res = ListNode(sum - 10)
                    over = 1
                else:
                    res = ListNode(sum)   
                res.next = helper(l1.next, None, over)
                return res
            else:
                sum = l1.val + l2.val + over
                over = 0
                if sum > 9:
                    res = ListNode(sum - 10)
                    over = 1
                else:
                    res = ListNode(sum)   
                res.next = helper(l1.next, l2.next, over)
                return res
        return helper(l1,l2)
                
            
        