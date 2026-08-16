class Solution:
    def longestPalindrome(self, s: str) -> str:
        size=len(s)
        l_palind=""
        for i in range(size):
            palind1=self.ispalindrome(i,i,s)
            palind2=self.ispalindrome(i,i+1,s)
            if len(palind1) >len(l_palind):
                l_palind=palind1
            if len(palind2)>len(l_palind):
                l_palind=palind2
        return l_palind



    def ispalindrome(self,i,j,s):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]

        

        