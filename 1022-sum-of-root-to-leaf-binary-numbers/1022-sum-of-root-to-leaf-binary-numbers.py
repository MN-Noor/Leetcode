# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else: return self.getBinary(0,root)
    def getBinary(self,tot,root):
        if root==None:
            return 0
        if not root.left and not root.right:
            return (tot <<1)|root.val
        else:
            tot=(tot<<1 )| root.val

        return self.getBinary(tot,root.left) + self.getBinary(tot,root.right)


        