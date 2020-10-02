import numpy as np
import sys

sys.setrecursionlimit(5000)


board_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


board_2 = [
    [1, 0, 0,  0, 0, 3,  6, 0, 0],
    [3, 0, 8,  0, 0, 0,  9, 0, 7],
    [0, 0, 4,  0, 0, 2,  0, 0, 8],

    [0, 0, 0,  5, 3, 0,  1, 4, 2],
    [0, 0, 7,  8, 6, 4,  5, 9, 0],
    [4, 0, 0,  0, 0, 1,  8, 0, 0],
    
    [7, 8, 1,  3, 4, 0,  0, 0, 0],
    [0, 0, 3,  0, 0, 6,  0, 0, 9],
    [0, 2, 9,  7, 5, 8,  4, 0, 0],
]

board_99 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


board_4 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 1, 7, 8, 9, 1, 2, 3],
    [5, 6, 4, 8, 9, 1, 0, 0, 0],
    [8, 9, 7, 9, 1, 2, 0, 0, 0],
    [7, 8, 9, 1, 2, 3, 0, 0, 0],
    [8, 9, 1, 2, 3, 4, 0, 0, 0],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def possible(y, x, n):

    global board

    for i in range(0,9):
        if board[y][i] == n:
            return False

    for i in range(0, 9):
        if board[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):

        for j in range(0, 3):

            if board[y0 + i][x0 + j] == n:

                return False
    return True


# count = 1


def solve():
    global board
    global count

    # count += 1
    # print(count)

    # print('starting solver')

    for b in range(9):

        for a in range(9):

            # print(b,a)

            if board[b][a] == 0:

                for n in range(1, 10):

                    if possible(b, a, n):

                        # print(a)

                        board[b][a] = n
                        # print(np.matrix(board))
                        solve()

                        board[b][a] = 0

                return

    print(np.matrix(board))


solve()

#print(np.matrix(board))

# print(np.matrix(board))

# print(np.matrix(board))


# ----------------solve rev 1 ------------
"""
def solve():
    global board
        
    for y in range(0,9):
            
        for x in range(0,9):
                
            if board[y][x] == 0:
                    
                for n in range (1,10):
                        
                    if possible(y,x,n):

                        board[y][x] = n

                        print(np.matrix(board))
                            
                        solve()

                    """

# Resutl

# [[2 3 4 7 1 5 6 8 9]
#  [1 5 6 2 4 3 7 9 0]
#  [7 8 9 4 3 6 2 0 1]
#  [8 9 0 1 2 4 5 3 6]
#  [0 0 8 5 6 9 0 2 4]
#  [9 0 0 3 7 0 4 1 8]
#  [3 0 5 9 8 1 0 4 2]
#  [4 0 2 0 9 7 8 5 0]
#  [5 4 0 0 0 0 3 6 7]]