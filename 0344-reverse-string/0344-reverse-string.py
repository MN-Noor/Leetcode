class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        def swap(l,r):
            if l>=r:
                return 
            s[l],s[r]=s[r],s[l]
            swap(l+1,r-1)
        swap(l,r)
        