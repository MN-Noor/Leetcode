class Solution:
    def reverseString(self, s: List[str]) -> None:
       self.substitute(s,0,len(s)-1)
    def substitute(self,s,l,r):
        if l>=r:
            return s
        temp=s[l]
        s[l]=s[r]
        s[r]=temp
        self.substitute(s,l+1,r-1)

        