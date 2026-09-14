class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            new_list = [x for x in board[i] if x != "."]

            if len(new_list) != len(set(new_list)):
                return False
            
        for j in range(9):
            new_list = [board[i][j] for i in range(9) if board[i][j] != "."]

            if len(new_list) != len(set(new_list)):
                return False

        for row in range(0,9,3):
            for col in range(0,9,3):
                new_list = []

                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]!=".":
                            new_list.append(board[i][j])
                if len(new_list) != len(set(new_list)):
                    return False
        return True



        