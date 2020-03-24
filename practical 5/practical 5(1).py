# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = 100
#ends when reach 1 for the first time
while n !=1:
    
    #list two situations
    if n%2 == 0:
       n=n/2
       print(n)
   
    elif n % 2 ==1:
       n = 3*n+1
       print(n)