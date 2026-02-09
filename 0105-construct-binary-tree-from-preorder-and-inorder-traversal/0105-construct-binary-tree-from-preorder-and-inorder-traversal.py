# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        root_value=preorder[0]
        root=TreeNode(preorder[0])
        mid=inorder.index(root_value)      
        leftin=inorder[:mid]
        rightin=inorder[mid+1:]
        leftpre=preorder[1:len(leftin)+1]
        rightpre=preorder[len(leftin)+1:]
        root.left=self.buildTree(leftpre,leftin)
        root.right=self.buildTree(rightpre,rightin)
        return root
