import random
import numpy as np
from matplotlib import pyplot as plt
def create_board():
    return np.zeros((3,3))


def place(board,player,position):
    if(board[position[0]][position[1]] == 0):
        board[position[0]][position[1]]=player
        return 1
    else:
        return 0

board=create_board()
if(place(board,1,(0,0))==0):
	print("Already placed")

def possibilities(board):
    x=np.where(board==0)
    y=list(zip(x[0],x[1]))
    return(y)
p=possibilities(board)


import random 
def random_place(board,player):
    x=possibilities(board)
    i,j=(random.choice(x))
    board[i][j]=player
    
random_place(board,1)


board = create_board()
for i in range(3):
    random_place(board,1)
    random_place(board,2)

def row_win(board,player):
    for i in range(3):
        if((board[i][0]==player) and (board[i][1]==player) and (board[i][2]==player)):
            return True
    return False

row_win(board,1)

def col_win(board,player):
    for i in range(3):
        if((board[0][i]==player) and (board[1][i]==player) and (board[2][i]==player)):
            return True
    return False

col_win(board,1)

board[1,1] = 2
def diag_win(board,player):
    if((board[0][0]==player and board[1][1]==player and board[2][2]==player)or(board[2][0]==player and board[1][1]==player and board[0][2]==player)):
        return True
    else:
        return False
diag_win(board,2)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if(row_win(board,player) or diag_win(board,player) or col_win(board,player)):
            winner=player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
evaluate(board)


def play_game():
    board=create_board()
    while(evaluate(board)==0):
        random_place(board,1)
        if(evaluate(board)==0):
            random_place(board,2)
    return evaluate(board)
m1=[0,0,0]
for i in range(1000):
    l=play_game()
    if(l==-1):
        m1[-1]+=1
    else:
        m1[l-1]+=1
print(m1)
def play_strategic_game():
    board=create_board()
    board[1][1]=1
    while(evaluate(board)==0):
        random_place(board,2)
        if(evaluate(board)==0):
            random_place(board,1)
    return evaluate(board)
m2=[0,0,0]
for i in range(1000):
    l=play_game()
    if(l==-1):
        m2[-1]+=1
    else:
        m2[l-1]+=1
print(m2)
minfo=['Player1','Player2','Draw']
plt.plot(m1,minfo,'*')
plt.plot(m2,minfo,'+')
plt.xlabel('No of Times')
plt.show()
