# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:08:46 2020

@author: 16977
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
re = seq[::-1]
reverse_seq = ''
for i in re:
    if i == 'A':
        reverse_seq+='T'
    elif i =='T':
        reverse_seq+='A'
    elif i =='C':
        reverse_seq+='G'
    elif i =='G':
        reverse_seq+='C'
print('The reverse complementary sequence is',reverse_seq)