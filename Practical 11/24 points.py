# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:55:23 2020

@author: 16977
"""

import re
from fractions import Fraction

re_numtest = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
i = 1
while i:
    i = 0
    data = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numList = data.split(',')
    for char in numList:
        if re_numtest.match(char): 
            continue
        else: 
            print('The input number must be intergers from 1 to 23')
            i = 1
            break

num = list(map(int,numList))  
L = num
def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:return x/y if y else None

def exp(p,iter=0):
    from itertools import permutations
    if len(p)==1:return [(p[0],str(p[0]))]
    operation = ['+','-','*','/']
    ret = []
    p = permutations(p) if iter==0 else [p]
    for array_n in p:
        #print(array_n)
        for num in range(1,len(array_n)):
            ret1 = exp(array_n[:num],iter+1)
            ret2 = exp(array_n[num:],iter+1)
            for op in operation:
                for va1,expression in ret1:
                    if va1==None:continue
                    for va2,expression2 in ret2:
                        if va2==None:continue
                        combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                        combined_exp += '{}' if expression2.isalnum() else '({})'
                        new_val = compute(va1,va2,op)
                        ret.append((new_val,combined_exp.format(expression,op,expression2)))
                        if iter==0 and new_val==24:
                            return ''.join(e+'\n' for x,e in ret if x==24)
    return ret
print(exp(L))

count = 0 

def dfs(n):
    global count
    count = count +1

    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            
            num[i] = a+b
            if(dfs(n-1)):
                return 1

            num[i] = a-b
            if(dfs(n-1)):
                return 1  

            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 

            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1  
            num[i] = a
            num[j] = b
    return 0 

if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)