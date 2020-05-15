# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:25:11 2020

@author: 16977
"""

human_file=open('SOD2_human.fa')
mouse_file=open('SOD2_mouse.fa')
random_file=open('RandomSeq.fa')
matrix_file=open('BLOSUM62.txt')
output=open('output.fa','w')
next(human_file)
next(mouse_file)
next(random_file)
next(matrix_file)
next(matrix_file)
next(matrix_file)
next(matrix_file)
next(matrix_file)
next(matrix_file)
human=human_file.read()
mouse=mouse_file.read()
random=random_file.read()
matrix=matrix_file.read()
human_file.close()
mouse_file.close()
random_file.close()
matrix_file.close()

import re
matrix=matrix.split('\n')
order_list=matrix[0]
order_list=order_list.lstrip()
order_list=re.split(r'\s+',order_list)


def ord(b):
    for t in range(1,24):
        if order_list[t-1]==b:
            return(t)
            break

def com(seq1,seq2,name1,name2):
    
    alignment=''
    score=0
    count=0
    
    for i in range(len(human)-1):
        order1=ord(seq1[i])
        order2=ord(seq2[i])
        line=matrix[order1]
        line=re.split(r'\s+',line)
        value=int(line[order2])
        if seq1[i]==seq2[i]:
            alignment+=seq1[i]
            count+=1
        elif value>=0:
            alignment+='+'
        else:
            alignment+=' '
        score+=value
    percentage=count/len(seq1)*100
    output.write(name1+'         '+seq1)
    output.write('alignment      '+alignment+'\n')
    output.write(name2+'         '+seq2+'\n')
    output.write('Score = '+str(score)+'\n')
    output.write('Percentage identity = '+str(percentage)+'%\n\n\n\n\n')


output.write('comparison between human and mouse\n\n')
com(human,mouse,'human ','mouse ')
output.write('comparison between human and random\n\n')
compare(human,random,'human ','random')
output.write('comparison between mouse and random\n\n')
compare(mouse,random,'mouse ','random')
output.close()