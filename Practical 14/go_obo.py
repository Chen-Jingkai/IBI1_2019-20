# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:49:57 2020

@author: 16977
"""

import xml.dom.minidom
import pandas as pd
DOMTree=xml.dom.minidom.parse('go_obo.xml')
collection=DOMTree.documentElement
terms=collection.getElementsByTagName('term')
Id=[]
Name=[]
Def=[]
childnodes=[]
def childnode(x):
    global terms
    childnodes=0
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        for parent in is_a:
            if parent.childNodes[0].data==x:
                childnodes+=1
                y=term.getElementsByTagName('id')[0].childNodes[0].data
                childnodes+=childnode(y)
    return childnodes
for term in terms:
    defs=term.getElementsByTagName('def')[0]
    defstr=defs.getElementsByTagName('defstr')[0].childNodes[0].data
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        x=term.getElementsByTagName('id')[0].childNodes[0].data
        Id.append(x)
        Name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        Def.append(defstr)
        childnodes.append(childnode(x))
file=pd.DataFrame({'id':Id,'name':Name,'definition':Def,'childnodes':childnode})
file.to_excel(r'C:\Li\IBI1_2019-20\Practical14\autophagosome.xlsx')
