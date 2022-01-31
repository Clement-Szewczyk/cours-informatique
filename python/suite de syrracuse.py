# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:30:10 2022

@author: Clément Szewczyk
"""

x=4
for _ in range(1000):
    if (x%2)==0:
        x=x/2
    else:
            x=x*3+1
    print(x)
