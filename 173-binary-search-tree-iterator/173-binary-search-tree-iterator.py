# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def generate(node) -> int:
            if node:
                yield from generate(node.left)
                yield(node.val)
                yield from generate(node.right)
                
        self.generator = generate(root)
        self.current = next(self.generator, None)
        

    def next(self) -> int:
        if not self.hasNext():
            return None
        next_value = self.current
        self.current = next(self.generator, None)
        return next_value
    
    
    def hasNext(self) -> bool:
        return False if self.current is None else True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()