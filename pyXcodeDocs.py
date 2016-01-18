# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:14:14 2016

@author: cycleuser

blog.cycleuser.org

This is a little script that gathers the links of Xcode Documents and puts all items into a single excel file.

You need to install pandas to run this script.

exam:
pip install pandas


"""



from pandas import DataFrame
import requests

link ="https://developer.apple.com/library/downloads/docset-index.dvtdownloadableindex"
file = requests.get(link)
fout = open('source.txt','w')
fout.write(file.text)
fout.close


names = []
links = []
result = ""
fin = open('source.txt','r')
lines = fin.readlines()

templines=[]
 
for j in range(0, len(lines)):
    templines.append(lines[j].strip())
 
 
for i in range(0, len(templines)):
    if "<key>name</key>" in templines[i]:
        if "none.dmg" not in templines[i+3]:
            names.append((templines[i+1])[8:-9])
            result += (templines[i+1])[8:-9] + "    ,"
        
    if "<key>source</key>" in lines[i]:
        if "none.dmg" not in templines[i+1]:
            links.append((templines[i+1])[8:-9])
            result += (templines[i+1])[8:-9] + "\n"

df = DataFrame({'Item names': names,'links': links})
df.to_excel('output.xlsx', sheet_name='sheet1', index=False)



















