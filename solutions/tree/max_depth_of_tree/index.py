# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
          return 0
        
        depth = 1
        
        def traverse(root,level):
          
          nonlocal depth
          
          if not root:
            return 
          
          traverse(root.left,level+1)
        
          
          if level > depth:
            depth = level
        
          traverse(root.right,level+1)
          
          return depth
          
        return traverse(root,1)
        