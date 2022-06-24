"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
                
        node_clones = {None : None}
        
        dummy = Node(0)
        tail_clone = dummy
        tail = head
        while tail:
            tail_clone.next = Node(tail.val)
            node_clones[tail] = tail_clone.next
            tail = tail.next
            tail_clone = tail_clone.next

        tail_clone = dummy.next
        tail = head
        while tail:
            tail_clone.next = node_clones[tail.next]
            tail_clone.random = node_clones[tail.random]
            tail = tail.next
            tail_clone = tail_clone.next
            

        return dummy.next  
            
                        
                
                
        
            
        
        
        