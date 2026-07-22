class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colHash = [set() for i in range(9)]
        rowHash = [set() for i in range(9)]
        boxHash = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in rowHash[i] or 
                board[i][j] in colHash[j] or 
                board[i][j] in boxHash[(i // 3) * 3 + (j // 3)]):
                    return False
                
                rowHash[i].add(board[i][j])
                colHash[j].add(board[i][j])
                boxHash[(i // 3) * 3 + (j // 3)].add(board[i][j])
        return True