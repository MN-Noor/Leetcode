# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size=len(s)
#         max_palind=0
#         l_palind=""
#         for i in range(size):
#             palind,word=self.ispalindrome(i,s)
#             if palind>max_palind:
#                 max_palind=palind
#                 l_palind=word
#         return l_palind



#     def ispalindrome(self,c,s):
#         i,j=c,c+1
#         size=1
#         index=0
#         flag=0
#         while i>0 and j<=len(s)-1 and flag<2:
#             if s[i]==s[j]:
#                 i-=1
#                 j+=1
#             if i%2==0:
#                 i-=1
#                 j+=1
#                 size+=2
#             else:
#                j+=1 
#                size+=1 
         
#         return size,s[i:j-1] 

        

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palind = ""

        for i in range(len(s)):
            # Odd-length palindrome
            word1 = self.ispalindrome(i, i, s)

            # Even-length palindrome
            word2 = self.ispalindrome(i, i + 1, s)

            if len(word1) > len(max_palind):
                max_palind = word1

            if len(word2) > len(max_palind):
                max_palind = word2

        return max_palind

    def ispalindrome(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1:j]