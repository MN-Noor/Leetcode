class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(Nopen,Nclose):
            if Nopen==Nclose==n:
                res.append("".join(stack))
                return
            if Nopen<n:
                stack.append('(')
                backtrack(Nopen+1,Nclose)
                stack.pop()
            if Nclose<Nopen:
                stack.append(')')
                backtrack(Nopen,Nclose+1)
                stack.pop()
                
        backtrack(0,0)
        return res

            



      