class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        p=0
        if l1>l2:
            return False
        while p<=l2-l1:
            n=s2[p:p+l1]
            if self.check_permutation(s1,n):
                return True
            p+=1
        return False 
    def check_permutation(self,s1,s2):
        hash={}
        for c in s1:
            hash[c]=hash.get(c,0)+1
        for c in s2:
            hash[c]=hash.get(c,0)-1
        for value in hash.values():
            if value!=0:
                return False
        return True 


        
        