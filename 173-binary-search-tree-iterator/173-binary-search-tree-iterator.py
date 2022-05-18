# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def inorder_generator(node) -> int:
            if node:
                yield from inorder_generator(node.left)
                yield(node.val)
                yield from inorder_generator(node.right)
                
        self.iterable = inorder_generator(root)
        self._next = next(self.iterable, None)
        

    def next(self) -> int:
        _next = self._next
        self._next = next(self.iterable, None)
        return _next
    
    
    def hasNext(self) -> bool:
        return self._next is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()