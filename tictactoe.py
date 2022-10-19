from array import *
import os

rows = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'a' : 0,
    'b' : 1,
    'c' : 2
}

def printBoard():
    print("A: " + board[0][0] + " " + board[0][1] + " " +  board[0][2] + "\nB: " +
          board[1][0] + " " + board[1][1] + " " + board[1][2] + "\nC: " +
          board[2][0] + " " + board[2][1] + " " + board[2][2] + "\n   1 2 3")

def move(row, column, player):
    board[row][column] = player

def checkIfWon(player):
    #check rows for wins
    if(board[0][0] == board[0][1] == board[0][2] == player):
        return True
    if(board[1][0] == board[1][1] == board[1][2] == player):
        return True
    if(board[2][0] == board[2][1] == board[2][2] == player):
        return True

    #check columns for wins
    if(board[0][0] == board[1][0] == board[2][0] == player):
        return True
    if(board[0][1] == board[1][1] == board[2][1] == player):
        return True
    if(board[0][2] == board[1][2] == board[2][2] == player):
        return True

    #check diagonals for wins
    if(board[0][0] == board[1][1] == board[2][2] == player):
        return True
    if(board[2][0] == board[1][1] == board[2][0] == player):
        return True
    
    

def playMove(currentPlayer):
    printBoard()
    print("\nPlayer " + currentPlayer + ": input what spot you want to take")
    playerInput = input()
    row = rows[playerInput[:1]]()
    column = int(playerInput[1:]) -1

    if(board[row][column] == empty):
        move(row, column, currentPlayer)
    else:
        print("Spot is taken. Please choose another spot:")
        playMove(currentPlayer)

    if(checkIfWon(currentPlayer)):
        print("player " + currentPlayer + " won.")
    elif(currentPlayer == 'X'):
        playMove('O')
    else:
        playMove('X')

    

empty = "-"
board = [[empty,empty,empty],[empty,empty,empty],[empty,empty,empty]]

playMove('X')


