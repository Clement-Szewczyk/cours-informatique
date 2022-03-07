# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:41:32 2022

@author: Clément Szewczyk
"""

def estabsente(serie,valeur):
    for n in range(0,len(serie)):
        if serie[n]==valeur:
            return False
    return True
    
'''
s = [2,3,4,5,0,20,33,11,35]
print(estabsente(s,9))
print(9 not in s)
'''
def recaman(maxi):
    serie=[]
    for n in range(0, maxi+1):
        if n ==0:
            valeur = 0
        elif serie[n-1]-n>0 and estabsente(serie, serie[n-1]-n):
            valeur = serie[n-1]-n
        else:
            valeur = serie[n-1]+n
        serie.append(valeur)
    return serie


print(recaman(10000))
