# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,minr,maxr):
            if not node:
                return True
            if minr!=None and node.val<=minr:
                return False
            if maxr!=None and node.val>=maxr:
                return False
            return dfs(node.left,minr,node.val) and dfs(node.right,node.val,maxr)
        return dfs(root,None,None)

          
        