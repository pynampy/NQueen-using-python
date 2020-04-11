board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

row = 0

def printboard(board):

    for i in board:
        print(i)


def valid(board,x,y):
    
    for i in range(4):
        if board[x][i] == 'Q' and y!=i:
            return False
        if board[i][y] == 'Q' and x!=i:
            return False
    

    for i in range(4):
        if x-i >= 0 and y + i < 4:
            if board[x-i][y+i] == 'Q':
                return False
        
        if x-i >= 0 and y-i >= 0:
            if board[x-i][y-i] == 'Q':
                return False

    return True


def solve(board,row):

    if row == 4:
        return True
        
    for i in range(0,4):
        
        if(valid(board,row,i))==True:
            
            board[row][i]='Q'
            row = row+1
            
            if solve(board,row) == True:
                return True
            
            row = row-1
            board[row][i]=0
            
            
    return False

solve(board,row)
printboard(board)