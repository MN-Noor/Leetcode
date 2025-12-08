class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp=0
        if not s:
            return True
        size=len(t)
        for tp in range(size):
            if s[sp]==t[tp]:
                sp+=1
            if sp==len(s):
                return True
        if sp==len(s):
            return True
        
        return False

        