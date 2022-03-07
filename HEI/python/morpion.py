# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:00:33 2022

@author: Clément Szewczyk
"""

def calculerscore(t):
    # check if horizontal win:
    for row in range(3):
        if (t[row][0]==t[row][1] and t[row][1]==t[row][2]):
            if t[row][0]=="X":
                return 10
        elif t[row][0]=="O":
            return -10
    #check if vertical win:
    for col in range(3):
        if (t[0][col]==t[1][col] and t[1][col]==t[2][col]):
            if t[0][col]=="X":
                return 10
        elif t[0][col]=="O":
            return -10
    #checking diagonals:
    if t[0][0] == t[1][1] and t[1][1] == t[2][2]:
        if t[0][0]=="X":
            return 10
        elif t[row][0]=="O":
            return -10
    if t[0][2] == t[1][1] and t[1][1] == t[2][0]:
        if t[0][0]=="X":
            return 10
        elif t[row][0]=="O":
            return -10
    # no one wins : return 0
    return 0

def meilleurMouvement(t):
    
    for i in range(3):
        for j in range(3):
            # if the place is free:
            if (t[i][j]=='_'):
                t[i][j]='X'
            nextMove = minmax(t,'O')
            
            if nextMove>bestMove:
                bestMove = (i,j)
                bestMove = nextMove
                
table = [
    ['X','O','O'],
    ['_','O','_'],
    ['O','X','X']]


