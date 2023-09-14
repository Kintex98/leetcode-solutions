board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def valid_val (row, col, val, board):
    for coordinate in range(9):
        # Checks the board
        if board[row][coordinate] == val:
            return False
        if board[coordinate][col] == val:
            return False
        if board[3*(row//3)+coordinate//3][3*(col//3)+coordinate%3] == val:
            return False
    return True

def iterate_board(board):
    for row in board:
        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    for val in range(1,10):
                        if valid_val(y,x,str(val), board):
                            board[y][x] = str(val)
                            if iterate_board(board):
                                return True
                            board[y][x] = '.'
                    return False
    return True
while not iterate_board(board):
    iterate_board(board)
print(board)