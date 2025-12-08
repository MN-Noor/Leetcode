class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.countNodes(0,0,text1,text2,hashmap={})
            

    def countNodes(self,i,j,text1,text2,hashmap):
        
        if i>=len(text1) or j>=len(text2):
            return 0
        if (i,j) in hashmap:
            return hashmap[i,j]
        if text1[i]==text2[j]:
            hashmap[(i,j)]= 1+self.countNodes(i+1,j+1,text1,text2,hashmap)
        else:
            hashmap[(i,j)]= max(self.countNodes(i+1,j,text1,text2,hashmap),self.countNodes(i,j+1,text1,text2,hashmap))
        return hashmap[(i,j)]

        