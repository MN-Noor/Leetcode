class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(r,c,wordmatch):
            if wordmatch==len(word):
                return True
            elif r<0 or r>=len(board) or c<0 or c>=len(board[0]):
                return False
            elif board[r][c]==word[wordmatch]:
                wordmatch+=1
                value=board[r][c]
                board[r][c]="#"
                find=search(r,c+1,wordmatch) or search(r+1,c,wordmatch) or search(r-1,c,wordmatch) or search(r,c-1,wordmatch)
                board[r][c]=value
                return find
            elif board[r][c]!=word[wordmatch]:
                return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i,j,0)==True:
                    return True
        return False