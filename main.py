import numpy as np


board = [
    [0,0,0,7,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,4,3,0,2,0,0],
    [0,0,0,0,0,0,0,0,6],
    [0,0,0,5,0,9,0,0,0],
    [0,0,0,0,0,0,4,1,8],
    [0,0,0,0,8,1,0,0,0],
    [0,0,2,0,0,0,0,5,0],
    [0,4,0,0,0,0,3,0,0],
]

def possible(y,x,n):

    global board

    for i in range(0,9):
        if board[y][i] == n:
            return False
    
    for j in range(0,9):
        if board[j][x] == n:
            return False
        
    x0 = (x //3 ) * 3
    y0 = (y // 3) * 3

    for i in range(0,3):
    
        for j in range(0,3):
    
            if board[x0 + i][y0+j] ==n:
    
                return False
    return True


def solve():
    global board
        
        for y in range(0,9):
            
            for x in range(0,9):
                
                if board[y][x] == 0:
                    
                    for n in range (1,10):
                        
                        if possible(y,x,n):

                            board[y][x] = n
                        
                            break
                        

                    
                
                


    print(np.matrix(board))




print (possible(4,4,5))




#print(np.matrix(board))