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
        elif t[0][0]=="O":
            return -10
    if t[0][2] == t[1][1] and t[1][1] == t[2][0]:
        if t[0][2]=="X":
            return 10
        elif t[0][2]=="O":
            return -10
    # no one wins : return 0
    return 0

def minmax(t,j):
    # calculer le score du je en cours:
    score = calculerscore(t)
    if score == 10 or score == -10:
        return score
   
    # X = aximizing player: 
    if j=='X':
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                # if the place is free:
                if (t[i][j]=='_'):
                    t[i][j]='X'
                    bestScore = max(bestScore, minmax(t,'O'))
                    t[i][j]='_'
        return bestScore
    else: 
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                # if the place is free:
                if (t[i][j]=='_'):
                    t[i][j]='O'
                    bestScore = min(bestScore, minmax(t,'O'))
                    t[i][j]='_'
        return bestScore
               

def meilleurMouvement(t):
    bestScore = -10000
    bestMove = (-1,-1)
    for i in range(3):
        for j in range(3):
            # if the place is free:
            if (t[i][j]=='_'):
                t[i][j]='X'
            nextScore = minmax(t,'O')
            
            if nextScore>bestScore:
                bestMove = (i,j)
                bestScore = nextScore
    print("Meilleur choix possible : ", bestMove, bestScore)
    return bestMove


table = [
    ['X','O','O'],
    ['_','_','_'],
    ['_','_','X']]


bestMove = meilleurMouvement(table)
print("the best move is ROW=%i COL=%i" % (bestMove[0], bestMove[1]))