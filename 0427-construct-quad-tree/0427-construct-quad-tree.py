"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
       n=len(grid)
       return self.isUniform(grid,0,0,n,n)
        

    def isUniform(self,grid,r1,c1,r2,c2):
        var=grid[r1][c1]
        for i in range(r1,r2):
            for j in range(c1,c2):
                if var!=grid[i][j]:
                    rm=(r1+r2)//2
                    cm=(c1+c2)//2
                    return Node(
                    isLeaf=False,
                    val=var,
                    topLeft=self.isUniform(grid,r1,c1,rm,cm),
                    topRight=self.isUniform(grid,r1,cm,rm,c2),
                    bottomLeft=self.isUniform(grid,rm,c1,r2,cm),
                    bottomRight=self.isUniform(grid,rm,cm,r2,c2))
        return Node(          
        isLeaf=True,
        val=var,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None)




        