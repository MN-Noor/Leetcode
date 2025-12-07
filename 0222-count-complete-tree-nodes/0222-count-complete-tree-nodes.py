# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depthleft=self.countDepth(root.left)#root 1 missing
        depthright=self.countDepth(root.right)
        if depthleft>depthright:
            return (1 << depthright)+self.countNodes(root.left)
        else:
            return (1 << depthleft)+self.countNodes(root.right)
        
    def countDepth(self,node):
        if not node:
            return 0
        return 1+self.countDepth(node.left)

        