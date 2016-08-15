# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:37:33 2016

@author: cycleuser
@email: cycleuser@cycleuser.org

Copyright 2016 cycleuser

"""
#!/usr/bin/env python

# coding=utf-8

lang = "python"



from pandas import DataFrame
import requests

link0 ="http://www.oreilly.com/data/free/archive.html"
link1="http://www.oreilly.com/programming/free/"
link2="http://www.oreilly.com/web-platform/free/"
link3="http://www.oreilly.com/iot/free/"
link4="http://www.oreilly.com/webops-perf/free/"
link5="http://www.oreilly.com/business/free/"

link =["http://www.oreilly.com/business/free/","http://www.oreilly.com/data/free/archive.html","http://www.oreilly.com/programming/free/","http://www.oreilly.com/web-platform/free/","http://www.oreilly.com/iot/free/","http://www.oreilly.com/webops-perf/free/"]


file=[]

for i in link:
    file.append(requests.get(i))


filewriter = open('source.txt','w')

for j in file:
    filewriter.write(j.text)

filewriter.close


names = []
links = []
result = ""


newf = open('source.txt','r')
filedata = newf.read()
newf.close()

newdata = filedata.replace('href="' ,'\n')
tmpdata = newdata.replace('free/' ,'free/files/')
newerdata = tmpdata.replace('.csp' ,'.mobi\n') #change mobi into pdf or epub if you need

f = open('newer.txt','w')
f.write(newerdata)
f.close()

f3 = open('newer.txt','r')
lines = f3.readlines()
templines=[]
 
for j in range(0, len(lines)):
    templines.append(lines[j].strip())
 
for i in range(0, len(templines)):
    if ".mobi" in templines[i]:                   #change mobi into pdf or epub if you need
        names.append((templines[i]))
        result += (templines[i]) + "    ,"

df = DataFrame({'Item names': names})
df.to_excel('output.xlsx', sheet_name='sheet1', index=False)




