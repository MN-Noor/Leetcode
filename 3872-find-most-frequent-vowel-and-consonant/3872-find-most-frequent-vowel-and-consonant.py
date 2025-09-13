class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vohashmap={}
        cohashmap={}
        for i in s:
            if i in "aeiou":
                vohashmap[i]=vohashmap.get(i,0)+1
            else:
                cohashmap[i]=cohashmap.get(i,0)+1

            vomax=max(vohashmap.values()) if vohashmap else 0
            comax=max(cohashmap.values()) if cohashmap else 0
        return vomax+comax


        